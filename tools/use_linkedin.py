# /tools/use_linkedin.py
"""This tool is used to get profile details, posts, search for people and companies on LinkedIn. You should read the tool's output results and see if they answer the user's question/fulfill the user's request, else try again and failing that, ask the user for more information. Note that the user's Linkedin username is `chrisboden`."""

import os
import sys
import argparse
import requests
import pandas as pd
from typing import List, Dict, Optional
from datetime import datetime, timedelta, timezone
from dateutil import parser
import json
import openai
from dotenv import load_dotenv
from termcolor import cprint
from pprint import pprint

# Load environment variables
load_dotenv()

# Number of days to look back for posts by default
DEFAULT_POST_AGE_DAYS = 30

class LinkedInAPI:
    """LinkedIn API wrapper for common operations with fallback support. This class provides methods to interact with LinkedIn's API through RapidAPI, offering access to profile details, posts, company information, and search functionality. It includes automatic fallback to alternative API endpoints if the primary endpoint fails."""
    
    def __init__(self):
        self.primary_url = "https://linkedin-api8.p.rapidapi.com"
        self.fallback_url = "https://linkedin-data-api.p.rapidapi.com"
        self.bulk_data_url = "https://linkedin-bulk-data-scraper.p.rapidapi.com"
        self.current_url = self.primary_url
        self.headers = {
            "X-RapidAPI-Host": "linkedin-api8.p.rapidapi.com",
            "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY")
        }
        self.bulk_headers = {
            "x-rapidapi-key": os.getenv("RAPIDAPI_KEY", ""),
            "x-rapidapi-host": "linkedin-bulk-data-scraper.p.rapidapi.com",
            "Content-Type": "application/json",
            "x-rapidapi-user": os.getenv("RAPIDAPI_USER", "")
        }

    def _update_api_host(self, use_fallback=False):
        """Update API host in headers based on current URL. This helper method switches between primary and fallback API endpoints when needed."""
        host = self.fallback_url.replace("https://", "") if use_fallback else self.primary_url.replace("https://", "")
        self.headers["X-RapidAPI-Host"] = host
        self.current_url = self.fallback_url if use_fallback else self.primary_url

    def _make_request(self, endpoint, params, fallback_attempted=False):
        """Make API request with fallback support. This helper method handles the API request process, automatically attempting to use the fallback API if the primary API fails."""
        try:
            url = f"{self.current_url}/{endpoint}"
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if not fallback_attempted:
                cprint(f"Primary API failed, attempting fallback: {str(e)}", "yellow")
                self._update_api_host(use_fallback=True)
                return self._make_request(endpoint, params, fallback_attempted=True)
            else:
                cprint(f"Both primary and fallback APIs failed: {str(e)}", "red")
                return None

    def get_profile(self, username):
        """Get comprehensive profile details for a LinkedIn user. This function retrieves detailed information about a LinkedIn profile including work history, education, skills, and other professional details. Use this when you need to analyze someone's professional background or verify their credentials.
        
        Args:
            username (str): The LinkedIn username (without the linkedin.com/in/ prefix)
        """
        return self._make_request("", {"username": username})

    def get_posts(self, username):
        """Get recent posts from a LinkedIn user's activity feed. This function retrieves the most recent content shared by a specific LinkedIn user. Use this to understand what topics someone is discussing, what content they're sharing, and how they're engaging with their network.
        
        Args:
            username (str): The LinkedIn username (without the linkedin.com/in/ prefix). Note that Chris Boden's username is `chrisboden`.
        """
        data = self._make_request("get-profile-posts", {"username": username})
        
        if not data:
            return None
            
        if not data.get("success"):
            cprint(f"Error: {data.get('message', 'Unknown error')}", "red")
            return None
            
        return data.get("data", [])

    def search_people(self, keywords="", first_name="", last_name="", company="", title="", location="", start=0):
        """Search for LinkedIn users with various filters. This function allows you to find LinkedIn profiles matching specific criteria such as name, company, job title, or location. Use this for recruiting, networking, finding experts in specific fields, or researching people at target companies.
        
        Args:
            keywords (str): General search terms
            first_name (str): First name filter
            last_name (str): Last name filter
            company (str): Company name filter
            title (str): Job title filter
            location (str): Geographic location filter
            start (int): Starting index for pagination
        """
        params = {
            "keywords": keywords,
            "firstName": first_name,
            "lastName": last_name,
            "company": company,
            "keywordTitle": title,
            "geo": location,
            "start": start
        }
        return self._make_request("search-people", params)

    def get_company(self, username):
        """Get detailed company information by LinkedIn username. This function retrieves comprehensive details about a company including industry, size, specialties, and other business information. Use this for company research, competitive analysis, or understanding potential business partners or employers.
        
        Args:
            username (str): The LinkedIn company username (without the linkedin.com/company/ prefix)
        """
        return self._make_request("get-company-details", {"username": username})
    
    def get_company_updates(self, company_urls, post_count=5, max_age_days=DEFAULT_POST_AGE_DAYS):
        """Fetch LinkedIn updates for multiple companies at once. This function retrieves recent posts from multiple LinkedIn company pages simultaneously and can filter them by age. Use this for monitoring competitors, tracking industry trends, or staying updated on multiple organizations of interest. The function can also generate AI-powered summaries of the updates if OpenRouter credentials are available.
        
        Args:
            company_urls (list): List of LinkedIn company URLs
            post_count (int): Number of recent posts to fetch per company (default: 5)
            max_age_days (int): Maximum age of posts to include in days (default: 30)
            
        Returns:
            Dict containing filtered company updates and metadata
        """
        try:
            # Define the API endpoint for the bulk company posts
            url = f"{self.bulk_data_url}/company_posts"
            
            # Prepare the payload with company URLs and post count
            payload = {
                "links": company_urls,
                "count": post_count
            }
            
            # Log API request details
            cprint(f"\n🌐 Making LinkedIn Bulk API request to: {url}", "blue")
            cprint(f"📦 Payload:", "blue")
            cprint(f"  - Number of companies: {len(company_urls)}", "blue")
            cprint(f"  - Posts per company: {post_count}", "blue")
            
            # Make a POST request to the LinkedIn Bulk API
            response = requests.post(url, json=payload, headers=self.bulk_headers)
            response.raise_for_status()
            
            # Log API response
            cprint(f"\n✅ LinkedIn API response received", "green")
            cprint(f"📊 Response status code: {response.status_code}", "green")
            
            # Parse the raw API response
            raw_updates = response.json()
            
            # Parse and filter the response
            filtered_updates = self._parse_linkedin_bulk_response(raw_updates, max_age_days)
            
            # Prepare the result dictionary with metadata
            result = {
                "timestamp": datetime.now().isoformat(),
                "status": "success",
                "post_age_days": max_age_days,
                "updates": filtered_updates
            }
            
            # Optionally generate summary if OpenRouter keys are available
            if os.getenv("OPENROUTER_API_KEY") and os.getenv("OPENROUTER_BASE_URL"):
                result["summary"] = self._generate_summary(filtered_updates, max_age_days)
                
            return result
            
        except Exception as e:
            # Log error details
            cprint(f"\n❌ Error during LinkedIn Bulk API request:", "red")
            cprint(f"  - Error type: {type(e).__name__}", "red")
            cprint(f"  - Error message: {str(e)}", "red")
            
            # Return an error result if the API request fails
            return {
                "timestamp": datetime.now().isoformat(),
                "status": "error",
                "error": str(e)
            }
    
    def _parse_linkedin_bulk_response(self, response_data, max_age_days):
        """Parse and filter the LinkedIn Bulk API response. This helper method processes the raw API response data from bulk company post requests, filtering out posts older than the specified maximum age and organizing the data into a standardized format for consistent handling throughout the application.
        
        Args:
            response_data (dict): Raw API response from the bulk company posts endpoint
            max_age_days (int): Maximum age of posts to include in days
        
        Returns:
            list: List of parsed and filtered company updates
        """
        # Calculate the cutoff date for filtering posts
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=max_age_days)
        cprint(f"\n📅 Filtering posts older than: {cutoff_date.strftime('%Y-%m-%d %H:%M:%S UTC')}", "blue")
        
        parsed_data = []
        
        # Iterate over each company's data in the response
        company_count = len(response_data.get('data', []))
        cprint(f"🏢 Processing {company_count} companies", "blue")
        
        for company_data in response_data.get('data', []):
            posts = company_data.get('posts', [])
            
            # Skip companies with no posts
            if not posts:
                continue
                
            filtered_posts = []
            company_name = posts[0]['actor']['actorName'] if posts else "Unknown Company"
            cprint(f"\n📊 Processing {company_name}:", "yellow")
            cprint(f"  - Total posts found: {len(posts)}", "yellow")
            
            # Filter posts based on the cutoff date
            for post in posts:
                post_date = parser.parse(post['postedAt'])
                if post_date > cutoff_date:
                    filtered_posts.append({
                        "post_text": post['postText'],
                        "post_date": post['postedAt']
                    })
                    cprint(f"  ✅ Including post from {post_date.strftime('%Y-%m-%d')}", "green")
                else:
                    cprint(f"  ❌ Skipping post from {post_date.strftime('%Y-%m-%d')} (too old)", "red")
                    
            # Only include companies with posts after filtering
            if filtered_posts:
                parsed_data.append({
                    "company": company_name,
                    "posts": filtered_posts
                })
                cprint(f"  📝 Kept {len(filtered_posts)} posts within date range", "cyan")
            else:
                cprint(f"  ℹ️ No posts within date range", "yellow")
        
        cprint(f"\n🎯 Final results:", "green")
        cprint(f"  - Companies processed: {company_count}", "green")
        cprint(f"  - Companies with recent posts: {len(parsed_data)}", "green")
        
        return parsed_data
    
    def _generate_summary(self, filtered_updates, max_age_days):
        """Generate an AI-powered summary of company updates using OpenRouter. This helper method creates a concise digest of the key points from multiple company posts, making it easier to understand trends and important announcements across multiple organizations.
        
        Args:
            filtered_updates (list): Filtered company updates to summarize
            max_age_days (int): Maximum age of posts included in days
            
        Returns:
            str: Markdown-formatted summary text of company updates
        """
        try:
            # Check for required environment variables
            if not os.getenv("OPENROUTER_API_KEY"):
                return "OpenRouter API key not found. Please set OPENROUTER_API_KEY environment variable."
            
            # Configure the OpenAI client with OpenRouter credentials
            client = openai.OpenAI(
                base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
                api_key=os.getenv("OPENROUTER_API_KEY")
            )
            
            # Prepare the prompt for the LLM
            prompt = f"Create a digest of the key updates from the following companies in the past {max_age_days} days:\n\n"
            
            # Add company updates to the prompt
            for company in filtered_updates:
                prompt += f"## {company['company']}:\n"
                for post in company['posts']:
                    prompt += f"- Posted on {post['post_date']}: {post['post_text'][:200]}...\n"
                prompt += "\n"
            
            # Make the API call to OpenRouter
            cprint("\n🤖 Generating summary using LLM...", "blue")
            response = client.chat.completions.create(
                model="google/gemini-2.0-flash-lite-001",  # Default model, can be configured
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that is able to analyse the posts made by companies we are interested in, on Linkedin. You then create an insightful and informative digest from those posts which helps us understand the key activities, achievements and announcements from those companies. No preamble required, just the md formatted digest. IMPORTANT: Linkedin allows companies to share posts made by other companies. It is very important that you get the hierarchy right when you interpret the post json. We are getting the posts for a list of named companies. A given company in that lists, eg Acme, has posts that it has made organically, posts that it reshares without comment (eg Acme shares a post by Amazon) and posts that it reshares with comment, eg Acme might say 'Love this new launch by Google <Google post below>'. You must put those posts under the heading of Acme, rather than under the heading of Amazon or Google (which are not companies in our list). Your digests are always in perfectly formatted markdown and include links to the original posts which are cleverly hyperlinked using relevant text in the digest items wherever possible, eg 'Radium discussed the true cost of capital in [a post](https://www.linkedin.com/posts/radium-capital-ltd_radium-discussed-the-true-cost-of-capital-in-activity-711800000000000000000000/) about financing for startups'"},
                    {"role": "user", "content": prompt}
                ]
            )
            
            summary = response.choices[0].message.content.strip()
            cprint("✅ Summary generated successfully", "green")
            return summary
            
        except Exception as e:
            # Print error message if summary generation fails
            cprint(f"❌ Error generating summary: {e}", "red")
            return "Error generating summary. Please check your OpenRouter configuration."

def fetch_company_urls_from_csv():
    """Fetch company LinkedIn URLs from a published CSV file. This function retrieves a list of LinkedIn company URLs from a CSV file specified in the COMPANIES_CSV_URL environment variable. Use this to easily manage and update the list of companies you want to monitor without changing the code.
    
    Returns:
        list: List of LinkedIn URLs for companies to monitor
    """
    try:
        # Retrieve the CSV URL from environment variables
        csv_url = os.getenv("COMPANIES_CSV_URL")
        cprint(f"\n🔍 Fetching companies from CSV:", "blue")
        cprint(f"  URL: {csv_url}", "blue")
        
        # Raise an error if the URL is not found
        if not csv_url:
            error_msg = "COMPANIES_CSV_URL not found in environment variables"
            cprint(f"❌ Error: {error_msg}", "red")
            raise ValueError(error_msg)
        
        # Read the CSV file into a DataFrame
        cprint(f"\n📥 Reading CSV data...", "blue")
        df = pd.read_csv(csv_url)
        
        # Log DataFrame info
        cprint(f"\n📊 CSV Data Info:", "yellow")
        cprint(f"  - Number of rows: {len(df)}", "yellow")
        cprint(f"  - Columns: {', '.join(df.columns)}", "yellow")
        
        # Check if 'Linkedin URL' column exists
        if 'Linkedin URL' not in df.columns:
            error_msg = "CSV is missing 'Linkedin URL' column. Available columns: " + ", ".join(df.columns)
            cprint(f"❌ Error: {error_msg}", "red")
            raise ValueError(error_msg)
        
        # Extract the LinkedIn URLs into a list
        company_urls = df['Linkedin URL'].dropna().tolist()
        
        # Log results
        cprint(f"\n✅ Successfully loaded company URLs:", "green")
        cprint(f"  - Total URLs found: {len(company_urls)}", "green")
        if company_urls:
            cprint("\n📝 First few URLs:", "cyan")
            for url in company_urls[:3]:
                cprint(f"  - {url}", "cyan")
            if len(company_urls) > 3:
                cprint(f"  - ... and {len(company_urls)-3} more", "cyan")
        else:
            cprint("⚠️ Warning: No URLs found in the CSV", "yellow")
        
        return company_urls
        
    except pd.errors.EmptyDataError:
        error_msg = "CSV file is empty"
        cprint(f"❌ Error: {error_msg}", "red")
        return []
    except Exception as e:
        # Print error message if fetching fails
        cprint(f"\n❌ Error fetching CSV:", "red")
        cprint(f"  - Error type: {type(e).__name__}", "red")
        cprint(f"  - Error message: {str(e)}", "red")
        return []

def format_post(post):
    """Format a LinkedIn post for human-readable display in the terminal. This function takes a LinkedIn post object and converts it into a well-structured, easy-to-read string format with all relevant information including date, text content, and engagement metrics.
    
    Args:
        post (dict): LinkedIn post data object
        
    Returns:
        str: Formatted post text for display
    """
    timestamp = post.get("postedDateTimestamp", 0) / 1000
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    return f"""
Date: {date}
Text: {post.get('text', 'No text content')}
Reactions: {post.get('totalReactionCount', 0)}
Comments: {post.get('commentsCount', 0)}
Reposts: {post.get('repostsCount', 0)}
URL: {post.get('postUrl', 'No URL available')}
{'-' * 80}"""

def format_profile(profile, verbose=False):
    """Format LinkedIn profile information for human-readable display. This function takes a LinkedIn profile object and presents the key information in a well-organized format, including personal details, work experience, education, and skills.
    
    Args:
        profile (dict): LinkedIn profile data object
        verbose (bool): Whether to show the full raw profile data
        
    Returns:
        None: Prints formatted profile information to the console
    """
    if verbose:
        cprint("\nFull Profile Data:", "green")
        pprint(profile)
        return

    cprint("\nProfile Summary:", "green")
    print(f"Name: {profile.get('firstName', '')} {profile.get('lastName', '')}")
    print(f"Headline: {profile.get('headline', '')}")
    print(f"Location: {profile.get('geo', {}).get('full', '')}")
    print(f"Summary: {profile.get('summary', '')}")
    
    if profile.get('educations'):
        cprint("\nEducation:", "green")
        for edu in profile['educations']:
            print(f"- {edu.get('schoolName', '')}: {edu.get('degree', '')} in {edu.get('fieldOfStudy', '')}")
            print(f"  ({edu.get('start', {}).get('year', '')} - {edu.get('end', {}).get('year', '')})")
    
    if profile.get('fullPositions'):
        cprint("\nWork Experience:", "green")
        for pos in profile['fullPositions']:
            print(f"\n- {pos.get('title', '')} at {pos.get('companyName', '')}")
            print(f"  {pos.get('start', {}).get('month', '')}/{pos.get('start', {}).get('year', '')} - "
                  f"{pos.get('end', {}).get('month', '') or 'Present'}/{pos.get('end', {}).get('year', '') or 'Present'}")
            if pos.get('description'):
                print(f"  Description: {pos.get('description', '')}")
            print(f"  Location: {pos.get('location', '')}")
    
    if profile.get('skills'):
        cprint("\nSkills:", "green")
        for skill in profile['skills']:
            print(f"- {skill.get('name', '')}: {skill.get('endorsementsCount', 0)} endorsements")

def format_company(company, verbose=False):
    """Format LinkedIn company information for human-readable display. This function takes a LinkedIn company object and presents the key information in a well-organized format, including company details, industry, size, and specialties.
    
    Args:
        company (dict): LinkedIn company data object
        verbose (bool): Whether to show the full raw company data
        
    Returns:
        None: Prints formatted company information to the console
    """
    if verbose:
        cprint("\nFull Company Data:", "green")
        pprint(company)
        return

    if not company or not company.get('data'):
        return

    data = company['data']
    cprint("\nCompany Details:", "green")
    print(f"Name: {data.get('name', '')}")
    print(f"Description: {data.get('description', '')}")
    print(f"Industry: {', '.join(data.get('industries', []))}")
    print(f"Website: {data.get('website', '')}")
    print(f"Followers: {data.get('followerCount', '')}")
    print(f"Specialties: {', '.join(data.get('specialties', []))}")
    if data.get('employeeCount'):
        print(f"Employee Count: {data['employeeCount']}")
    if data.get('headquarters'):
        print(f"Headquarters: {data['headquarters']}")

def format_company_updates(updates, output_format="text", output_file=None, verbose=False):
    """Format LinkedIn company updates for display or output to a file. This function takes company updates data and presents it in either text or JSON format, with options to save to a file or display in the console.
    
    Args:
        updates (dict): Company updates data
        output_format (str): Format for output ('text' or 'json')
        output_file (str): Optional file path to write output
        verbose (bool): Whether to show the full raw updates data
        
    Returns:
        None: Prints or saves formatted company updates
    """
    if verbose:
        cprint("\nFull Company Updates Data:", "green")
        pprint(updates)
        return
    
    if updates.get("status") == "error":
        cprint(f"Error fetching company updates: {updates.get('error', 'Unknown error')}", "red")
        return
    
    if output_format == "json":
        # Output as JSON
        output_data = json.dumps(updates, indent=2)
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(output_data)
                cprint(f"✅ Company updates saved to {output_file}", "green")
            except Exception as e:
                cprint(f"❌ Error saving to file: {e}", "red")
                print(output_data)
        else:
            print(output_data)
    else:
        # Output as formatted text
        cprint(f"\n== LinkedIn Company Updates ==", "green")
        cprint(f"Timestamp: {updates.get('timestamp')}", "cyan")
        cprint(f"Post Age Filter: {updates.get('post_age_days')} days", "cyan")
        
        # Print summary if available
        if updates.get("summary"):
            cprint(f"\n== SUMMARY ==", "yellow")
            print(updates.get("summary"))
            cprint(f"==============", "yellow")
        
        # Print updates for each company
        for company in updates.get("updates", []):
            cprint(f"\n## {company['company']} ##", "blue")
            for i, post in enumerate(company.get("posts", [])):
                cprint(f"\nPost #{i+1} - {post.get('post_date')}", "green")
                print(f"{post.get('post_text')}")
                print("-" * 80)
        
        # Save to file if specified
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(f"== LinkedIn Company Updates ==\n")
                    f.write(f"Timestamp: {updates.get('timestamp')}\n")
                    f.write(f"Post Age Filter: {updates.get('post_age_days')} days\n\n")
                    
                    if updates.get("summary"):
                        f.write(f"== SUMMARY ==\n")
                        f.write(f"{updates.get('summary')}\n")
                        f.write(f"==============\n\n")
                    
                    for company in updates.get("updates", []):
                        f.write(f"## {company['company']} ##\n")
                        for i, post in enumerate(company.get("posts", [])):
                            f.write(f"\nPost #{i+1} - {post.get('post_date')}\n")
                            f.write(f"{post.get('post_text')}\n")
                            f.write("-" * 80 + "\n")
                
                cprint(f"✅ Company updates saved to {output_file}", "green")
            except Exception as e:
                cprint(f"❌ Error saving to file: {e}", "red")

def main():
    """Command-line interface for the LinkedIn API tool. This function parses command-line arguments and executes the appropriate LinkedIn API operations based on the specified action.
    
    Available actions:
    - profile: Get comprehensive profile details for a LinkedIn user
    - posts: Get recent posts from a LinkedIn user's activity feed
    - search: Search for LinkedIn users with various filters
    - company: Get detailed company information by LinkedIn username
    - updates: Fetch LinkedIn updates for multiple companies at once
    
    Each action supports specific parameters as documented in the help text, and all actions support a --verbose flag to show full raw data.
    """
    parser = argparse.ArgumentParser(description='LinkedIn API Tool')
    subparsers = parser.add_subparsers(dest='action', help='Action to perform')
    
    # Profile parser
    profile_parser = subparsers.add_parser('profile', help='Get LinkedIn profile')
    profile_parser.add_argument('--username', required=True, help='LinkedIn username')
    profile_parser.add_argument('--verbose', '-v', action='store_true', help='Show full raw data')
    
    # Posts parser
    posts_parser = subparsers.add_parser('posts', help='Get LinkedIn posts')
    posts_parser.add_argument('--username', required=True, help='LinkedIn username')
    posts_parser.add_argument('--verbose', '-v', action='store_true', help='Show full raw data')
    
    # Search parser
    search_parser = subparsers.add_parser('search', help='Search LinkedIn')
    search_parser.add_argument('--keywords', help='Search keywords')
    search_parser.add_argument('--first-name', help='First name for search')
    search_parser.add_argument('--last-name', help='Last name for search')
    search_parser.add_argument('--company', help='Company name for search')
    search_parser.add_argument('--title', help='Job title for search')
    search_parser.add_argument('--location', help='Location for search')
    search_parser.add_argument('--start', type=int, default=0, help='Start index for search results')
    search_parser.add_argument('--verbose', '-v', action='store_true', help='Show full raw data')
    
    # Company parser
    company_parser = subparsers.add_parser('company', help='Get LinkedIn company details')
    company_parser.add_argument('--username', required=True, help='LinkedIn company username')
    company_parser.add_argument('--verbose', '-v', action='store_true', help='Show full raw data')
    
    # Company updates parser
    updates_parser = subparsers.add_parser('updates', help='Get LinkedIn company updates')
    updates_parser.add_argument('--urls', nargs='+', help='List of LinkedIn company URLs')
    updates_parser.add_argument('--csv', action='store_true', help='Fetch company URLs from CSV defined in COMPANIES_CSV_URL env var')
    updates_parser.add_argument('--post-count', type=int, default=5, help='Number of posts to fetch per company')
    updates_parser.add_argument('--max-age', type=int, default=DEFAULT_POST_AGE_DAYS, help='Max age of posts in days')
    updates_parser.add_argument('--format', choices=['text', 'json'], default='text', help='Output format')
    updates_parser.add_argument('--output', help='Output file path')
    updates_parser.add_argument('--verbose', '-v', action='store_true', help='Show full raw data')
    
    args = parser.parse_args()
    
    if not os.getenv("RAPIDAPI_KEY"):
        cprint("Error: RAPIDAPI_KEY environment variable not set", "red")
        sys.exit(1)
    
    api = LinkedInAPI()
    
    if args.action == 'profile' and args.username:
        profile = api.get_profile(args.username)
        if profile:
            format_profile(profile, args.verbose)
            
    elif args.action == 'posts' and args.username:
        posts = api.get_posts(args.username)
        if posts:
            if args.verbose:
                cprint("\nFull Posts Data:", "green")
                pprint(posts)
            else:
                cprint(f"\nRecent Posts from {args.username}:", "green")
                print("=" * 80)
                for post in posts:
                    print(format_post(post))
                
    elif args.action == 'search':
        results = api.search_people(
            keywords=args.keywords,
            first_name=args.first_name,
            last_name=args.last_name,
            company=args.company,
            title=args.title,
            location=args.location,
            start=args.start
        )
        if args.verbose:
            cprint("\nFull Search Results:", "green")
            pprint(results)
        elif results and results.get('data', {}).get('items'):
            for person in results['data']['items']:
                print(f"\nName: {person.get('fullName')}")
                print(f"Headline: {person.get('headline')}")
                print(f"Location: {person.get('location')}")
                print(f"Profile: {person.get('profileURL')}")
                
    elif args.action == 'company' and args.username:
        company = api.get_company(args.username)
        format_company(company, args.verbose)
        
    elif args.action == 'updates':
        # Get company URLs from CSV if specified
        if args.csv:
            company_urls = fetch_company_urls_from_csv()
        elif args.urls:
            company_urls = args.urls
        else:
            cprint("Error: Either --urls or --csv must be specified", "red")
            sys.exit(1)
            
        # Fetch company updates
        updates = api.get_company_updates(
            company_urls=company_urls,
            post_count=args.post_count,
            max_age_days=args.max_age
        )
        
        # Format and display results
        format_company_updates(
            updates=updates,
            output_format=args.format,
            output_file=args.output,
            verbose=args.verbose
        )

if __name__ == "__main__":
    main() 