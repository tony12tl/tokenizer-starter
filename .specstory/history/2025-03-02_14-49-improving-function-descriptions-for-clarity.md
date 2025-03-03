## SpecStory

## Improving Function Descriptions for Clarity (02/03/2025, 14:49:29)

_**User**_

i want to make sure the descriptions for each function are well explained. i have taken content from the doc string atop the file and improved the descriptions for the `likes` and `lists` functions, please do the others

---

_**Assistant**_

I'll help you improve the function descriptions for the other functions in the Twitter API tool. Let me first examine the current descriptions and then enhance them to be more informative and consistent with the improvements you've already made for the `likes` and `lists` functions.

---

_****_

Read file: tools/use_twitter.py

---

_****_

Read file: tools/use_twitter.py

---

_****_



Now I'll update the function descriptions to be more informative and consistent with the improvements you've already made for the `likes` and `lists` functions.

---

_****_

```diff
  
      def get_user_tweets(self, username, limit=10, include_replies=False, include_pinned=False):
-         """Get tweets from a specific user"""
+         """Get tweets from a specific Twitter user's timeline. Use this function when you need to retrieve the most recent tweets posted by a particular user. This is useful for checking what specific individuals or organizations have been posting about recently.
+         
+         Args:
+             username (str): The Twitter username (without the @ symbol)
+             limit (int): Maximum number of tweets to retrieve (default: 10)
+             include_replies (bool): Whether to include reply tweets in the results (default: False)
+             include_pinned (bool): Whether to include pinned tweets in the results (default: False)
+         """
          url = f"{self.base_url}/user/tweets"
          params = {
```

---

_****_



Now let's update the search_tweets function to be more descriptive while maintaining the existing parameter documentation:

---

_****_

```diff
      def search_tweets(self, query, section="latest", min_retweets=0, min_likes=0, limit=10, 
                       start_date=None, end_date=None, language=None):
-         """Search for tweets based on various criteria
+         """Search for tweets based on keywords, hashtags, or phrases. Use this function when you need to find tweets about specific topics, events, or discussions happening on Twitter. This is particularly useful for researching trending topics, gathering opinions, or monitoring conversations around specific subjects.
          
          Args:
```

---

_****_



Now let's update the helper methods that extract tweets from different API responses to be more descriptive:

---

_****_

```diff
  
      def _extract_tweet_data(self, tweet_data):
-         """Extract relevant data from a single tweet"""
+         """Extract relevant data from a single tweet object returned by the Twitter API. This helper method parses the complex Twitter API response structure and extracts the most important tweet information into a clean, standardized format."""
          if not tweet_data:
              return None
  
      def _extract_tweets_from_user(self, data):
-         """Extract tweets from user timeline response"""
+         """Extract and normalize tweets from a user timeline API response. This helper method processes the raw API response data from user timeline requests and converts it into a standardized tweet format for consistent handling throughout the application."""
          tweets = []
          try:
  
      def _extract_tweets_from_search(self, data):
-         """Extract tweets from search response"""
+         """Extract and normalize tweets from a search API response. This helper method processes the raw API response data from search requests and converts it into a standardized tweet format for consistent handling throughout the application."""
          tweets = []
          try:
  
      def _extract_tweets_from_list(self, data):
-         """Extract tweets from list response"""
+         """Extract and normalize tweets from a Twitter list API response. This helper method processes the raw API response data from list requests and converts it into a standardized tweet format for consistent handling throughout the application."""
          tweets = []
          try:
```

---

_****_





Finally, let's update the format_tweet function to be more descriptive:

---

_****_

```diff
  
  def format_tweet(tweet):
-     """Format a tweet for display"""
+     """Format a tweet for human-readable display in the terminal. This function takes a standardized tweet object and converts it into a well-structured, easy-to-read string format with all relevant tweet information including date, author, text content, media, URLs, and engagement metrics. The formatted output is designed for terminal display with clear section separators."""
      try:
          date = datetime.strptime(tweet.get("created_at"), "%a %b %d %H:%M:%S +0000 %Y").strftime('%Y-%m-%d %H:%M:%S')
```

---

_****_





Let's also update the main function to provide a better description of the command-line interface:

---

_****_

```diff
  
  def main():
+     """Command-line interface for the Twitter API tool. This function parses command-line arguments and executes the appropriate Twitter API operations based on the specified action. 
+     
+     Available actions:
+     - user-tweets: Get tweets from a specific user's timeline
+     - search: Search for tweets based on keywords, hashtags, or phrases
+     - list-tweets: Get tweets from a specific Twitter list
+     - likes: Get tweets that a user has liked/favorited
+     
+     Each action requires specific parameters as documented in the help text.
+     """
      parser = argparse.ArgumentParser(description='Twitter API Tool')
      parser.add_argument('action', choices=['user-tweets', 'search', 'list-tweets', 'likes'],
```

---

_****_



I've updated all the function descriptions in the Twitter API tool to be more informative and consistent with the improvements you already made for the `likes` and `lists` functions. Here's a summary of the changes:

1. **get_user_tweets**: Enhanced the description to explain when and why you would use this function, and added detailed parameter documentation.

2. **search_tweets**: Expanded the description to explain the purpose and use cases for searching tweets, while maintaining the existing parameter documentation.

3. **Helper methods** (_extract_tweet_data, _extract_tweets_from_user, _extract_tweets_from_search, _extract_tweets_from_list): Added detailed descriptions explaining that these are helper methods that process and normalize the raw API responses into a standardized format.

4. **format_tweet**: Improved the description to explain that this function formats tweet data for human-readable terminal display with all relevant information.

5. **main**: Added a comprehensive description of the command-line interface, including available actions and their purposes.

All the function descriptions now follow a consistent style and provide more context about when and why to use each function, making the code more maintainable and easier to understand. The descriptions also highlight the relationship between different functions and how they work together in the overall workflow of the Twitter API tool.

---

_**User**_

please do same for linkedin tool (improve command descriptions). use info from doc below where helpful

-----

# LinkedIn API Tool Guide

A Python CLI tool for interacting with LinkedIn's API through RapidAPI. This tool provides rich data about profiles, companies, and posts.

## Setup

1. Install requirements:
```bash
pip install requests python-dotenv termcolor pandas python-dateutil
```

2. Set your RapidAPI key in .env:
```
RAPIDAPI_KEY=your_key_here
```

3. Optional: For summary generation, set OpenRouter credentials:
```
OPENROUTER_API_KEY=your_openrouter_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

4. Optional: For company URL retrieval from CSV:
```
COMPANIES_CSV_URL=https://your-csv-url.com/companies.csv
```

## Key Features

- Comprehensive profile data including work history, education, skills
- Company information including industry, size, and specialties
- Recent posts with engagement metrics
- Search functionality with multiple filters
- Bulk company updates from multiple companies at once
- CSV integration for company lists
- AI-powered summary generation for company updates
- Verbose mode to see raw API data

## Usage

The tool now supports five main actions, each with a --verbose (-v) flag to show full raw data:

### 1. Get Profile Details
```bash
# Get formatted profile summary
python3 tools/use_linkedin_api.py profile --username <username>

# Get full raw profile data
python3 tools/use_linkedin_api.py profile --username <username> --verbose
```

Profile data includes:
- Basic Info (name, headline, location)
- Full work history with dates and descriptions
- Education details
- Skills with endorsement counts
- Languages
- Summary
- Profile picture URLs
- Background image URLs

### 2. Get Recent Posts
```bash
# Get formatted posts
python3 tools/use_linkedin_api.py posts --username <username>

# Get full raw post data
python3 tools/use_linkedin_api.py posts --username <username> --verbose
```

Post data includes:
- Post text
- Timestamps
- Engagement metrics (likes, comments, shares)
- URLs
- Media attachments

### 3. Search People
```bash
python3 tools/use_linkedin_api.py search [options]
Options:
  --keywords "search terms"
  --first-name "John"
  --last-name "Doe"
  --company "Company Name"
  --title "Job Title"
  --location "Location"
  --start 0
  --verbose
```

Search results include:
- Basic profile information
- Current role
- Location
- Profile URL

### 4. Get Company Details
```bash
# Get formatted company info
python3 tools/use_linkedin_api.py company --username <company_username>

# Get full raw company data
python3 tools/use_linkedin_api.py company --username <company_username> --verbose
```

Company data includes:
- Name and description
- Industry and specialties
- Website
- Follower count
- Employee count
- Headquarters location

### 5. Get Multiple Company Updates
```bash
# Get updates from specific company URLs
python3 tools/use_linkedin_api.py updates --urls https://linkedin.com/company/company1 https://linkedin.com/company/company2

# Get updates from companies in a CSV file
python3 tools/use_linkedin_api.py updates --csv

# Customize post count and age filter
python3 tools/use_linkedin_api.py updates --csv --post-count 10 --max-age 60

# Output as JSON to a file
python3 tools/use_linkedin_api.py updates --csv --format json --output company_updates.json

# Get full raw updates data
python3 tools/use_linkedin_api.py updates --urls <company_urls> --verbose
```

Company updates features:
- Fetch posts from multiple companies simultaneously
- Filter posts by age (default 30 days)
- Generate AI summaries of updates (requires OpenRouter credentials)
- Export to JSON or formatted text
- Save to file

## Example Use Cases

### 1. Full Profile Analysis
```bash
# Get complete profile information
python3 tools/use_linkedin_api.py profile --username lucpettett --verbose

# Get their recent posts
python3 tools/use_linkedin_api.py posts --username lucpettett

# Get details about their current company
python3 tools/use_linkedin_api.py company --username telescope-co
```

### 2. Company Research
```bash
# Get company details
python3 tools/use_linkedin_api.py company --username peregianhub --verbose

# Search for employees
python3 tools/use_linkedin_api.py search --company "Peregian Digital Hub" --location "Sunshine Coast"
```

### 3. Monitor Multiple Companies
```bash
# Track updates from Peregian companies
python3 tools/use_linkedin_api.py updates --urls https://linkedin.com/company/peregianhub https://linkedin.com/company/other-company --max-age 14

# Get updates from CSV list and save to file
python3 tools/use_linkedin_api.py updates --csv --output peregian_updates.txt

# Generate a summary report in JSON format
python3 tools/use_linkedin_api.py updates --csv --format json --output updates_report.json
```

## CSV Format for Company URLs

When using the `--csv` option, the tool expects a CSV file with a column named "Linkedin URL" containing the full LinkedIn company page URLs. The URL to this CSV should be defined in the environment variable `COMPANIES_CSV_URL`.

Example CSV format:
```
Company Name,Linkedin URL,Other Columns
Company 1,https://linkedin.com/company/company1,data
Company 2,https://linkedin.com/company/company2,data
```

## Important IDs

Chris Boden's linkedin username is `chrisboden`
The Peregian Digital Hub's company name is `peregianhub`

## Best Practices

1. Always check the full data first with --verbose to understand what's available
2. Use multiple endpoints to gather comprehensive information
3. When profiling someone:
   - Start with profile data
   - Check their recent posts
   - Look up their company
   - Search for additional context
4. When tracking multiple companies:
   - Use the updates command with the --csv option for convenience
   - Filter by age to get only recent posts
   - Save outputs to files for historical comparison
5. Use the formatted output for quick overview, verbose mode for detailed analysis

## Notes

- All API calls require a valid RapidAPI key in .env
- Summary generation requires OpenRouter credentials
- Results are color-coded for better readability
- Error handling is built in with clear messages
- Rate limits apply based on RapidAPI plan
- The tool will gracefully handle missing data fields

---

_**Assistant**_

I'll improve the command descriptions for the LinkedIn tool, using the information from the provided guide to make them more informative and consistent with the Twitter tool's improved descriptions.

Let me update the function descriptions in the LinkedIn API tool:

---

_****_

```diff
  
  class LinkedInAPI:
-     """LinkedIn API wrapper for common operations with fallback support"""
+     """LinkedIn API wrapper for common operations with fallback support. This class provides methods to interact with LinkedIn's API through RapidAPI, offering access to profile details, posts, company information, and search functionality. It includes automatic fallback to alternative API endpoints if the primary endpoint fails."""
      
      def __init__(self):
```

---

_****_



Now let's update the descriptions for the main API methods:

---

_****_



---

_****_



---



---

