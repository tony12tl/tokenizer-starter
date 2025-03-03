# tools/use_twitter.py

"""
The user is an avid user of Twitter/X. It is where they get their news, etc. They have some key lists they follow and they use Twitter favorites as their bookmarks for things they find interesting. So when they ask you about information or news you should use this tool. For example, if they say they want to know what's happening with AI this week, you should use the get_list_tweets function with the list id `1609883077026918400` to get the tweets from the list for the last 7 days. If they say 'what have I found interesting this week', you should use the get_user_likes function to get the tweets from the user's favorites for the last 7 days.

This tool is used to get user tweets, search tweets, and access Twitter lists via RapidAPI. 

Make sure to include links to tweets when creating notes/emails/etc

Important Lists

The user follows the following important Twitter lists:

- `1609883077026918400`: Tweets from people I follow that are into AI and Tech
- `1890266787457200309`: Tweets by vibe coders (people coding with AI)
- `1848574231556346230`: Tweets by the major AI vendors (Openai, anthropic, etc)

"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime
from dotenv import load_dotenv
from termcolor import cprint

# Load environment variables
load_dotenv()

def clean_env_var(var_name):
    """Clean environment variable by removing newlines and extra whitespace"""
    value = os.getenv(var_name, '')
    if value:
        # Remove newlines and extra whitespace
        value = ' '.join(value.split())
    return value

class TwitterAPI:
    """Twitter API wrapper for common operations"""
    
    def __init__(self):
        self.base_url = "https://twitter154.p.rapidapi.com"
        self.headers = {
            "X-RapidAPI-Host": "twitter154.p.rapidapi.com",
            "X-RapidAPI-Key": clean_env_var("RAPIDAPI_KEY")
        }
        
        # Add headers for direct Twitter API access with cleaned values
        auth = clean_env_var("HEADER_AUTHORIZATION")
        cookies = clean_env_var("HEADER_COOKIES")
        csrf = clean_env_var("HEADER_CSRF")
        
        # Debug auth headers
        cprint("\nChecking Twitter API credentials:", "blue")
        cprint(f"Authorization length: {len(auth) if auth else 0}", "blue")
        cprint(f"Cookies length: {len(cookies) if cookies else 0}", "blue")
        cprint(f"CSRF length: {len(csrf) if csrf else 0}", "blue")
        
        self.twitter_headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Authorization': auth,
            'Accept-Language': 'en-US,en;q=0.9',
            'Host': 'api.twitter.com',
            'Origin': 'https://twitter.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
            'Referer': 'https://twitter.com/',
            'Connection': 'keep-alive',
            'Cookie': cookies,
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en',
            'x-csrf-token': csrf,
            'x-twitter-auth-type': 'OAuth2Session'
        }

    def get_user_tweets(self, username, limit=10, include_replies=False, include_pinned=False):
        """Get tweets from a specific Twitter user's timeline. Use this function when you need to retrieve the most recent tweets posted by a particular user. This is useful for checking what specific individuals or organizations have been posting about recently.
        
        Args:
            username (str): The Twitter username (without the @ symbol)
            limit (int): Maximum number of tweets to retrieve (default: 10)
            include_replies (bool): Whether to include reply tweets in the results (default: False)
            include_pinned (bool): Whether to include pinned tweets in the results (default: False)
        """
        url = f"{self.base_url}/user/tweets"
        params = {
            "username": username,
            "limit": limit,
            "include_replies": include_replies,
            "include_pinned": include_pinned
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Debug response structure if no results
            if not data or 'results' not in data:
                cprint(f"Unexpected response structure: {str(data)[:200]}...", "yellow")
                return None
                
            return self._extract_tweets_from_user(data)
        except Exception as e:
            cprint(f"Error fetching user tweets: {str(e)}", "red")
            return None

    def search_tweets(self, query, section="latest", min_retweets=0, min_likes=0, limit=10, 
                     start_date=None, end_date=None, language=None):
        """Search for tweets based on keywords, hashtags, or phrases. Use this function when you need to find tweets about specific topics, events, or discussions happening on Twitter. This is particularly useful for researching trending topics, gathering opinions, or monitoring conversations around specific subjects.
        
        Args:
            query (str): The search query
            section (str): Section to search in ('top', 'latest', 'people', 'photos', 'videos')
            min_retweets (int): Minimum number of retweets
            min_likes (int): Minimum number of likes
            limit (int): Number of results to return
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            language (str): Language code (e.g., 'en')
        """
        url = f"{self.base_url}/search/search"
        
        # Validate section parameter
        valid_sections = ['top', 'latest', 'people', 'photos', 'videos']
        if section not in valid_sections:
            cprint(f"Invalid section: {section}. Must be one of: {', '.join(valid_sections)}", "red")
            return None
            
        params = {
            "query": query,
            "section": section,
            "min_retweets": min_retweets,
            "min_likes": min_likes,
            "limit": limit
        }
        
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if language:
            params["language"] = language
            
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Debug response structure if no results
            if not data or 'results' not in data:
                cprint(f"Unexpected response structure: {str(data)[:200]}...", "yellow")
                return None
                
            return self._extract_tweets_from_user(data)
        except Exception as e:
            cprint(f"Error searching tweets: {str(e)}", "red")
            return None

    def get_list_tweets(self, list_id, limit=10):
        """Get tweets from a specific Twitter list. The user follows the following important Twitter lists:
        - `1609883077026918400`: Tweets from people the user follows that are into AI and Tech
        - `1890266787457200309`: Tweets by vibe coders (people coding with AI)
        - `1848574231556346230`: Tweets by the major AI vendors (Openai, anthropic, etc)"""
        url = f"{self.base_url}/lists/tweets"
        params = {
            "list_id": list_id,
            "limit": limit
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Debug response structure if no results
            if not data or 'results' not in data:
                cprint(f"Unexpected response structure: {str(data)[:200]}...", "yellow")
                return None
                
            return self._extract_tweets_from_user(data)
        except Exception as e:
            cprint(f"Error fetching list tweets: {str(e)}", "red")
            return None

    def get_user_likes(self, user_id, limit=100):
        """Get likes/favorites for a user directly from Twitter API. The user uses Twitter favorites as their bookmarks for things they find interesting or want to recall for future research or work. So if they say 'what have I found interesting this week', you should use the get_user_likes function to get the tweets from the user's favorites for the last 7 days. The user's id USER_ID=8356"""
        likes_url = 'https://api.twitter.com/graphql/QK8AVO3RpcnbLPKXLAiVog/Likes'
        
        variables_data = {
            "userId": user_id,
            "count": limit,
            "includePromotedContent": False,
            "withSuperFollowsUserFields": False,
            "withDownvotePerspective": False,
            "withReactionsMetadata": False,
            "withReactionsPerspective": False,
            "withSuperFollowsTweetFields": False,
            "withClientEventToken": False,
            "withBirdwatchNotes": False,
            "withVoice": False,
            "withV2Timeline": True
        }
        
        features_data = {
            "responsive_web_twitter_blue_verified_badge_is_enabled": True,
            "verified_phone_label_enabled": False,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "view_counts_public_visibility_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "responsive_web_twitter_article_tweet_consumption_enabled": True,
            "tweetypie_unmention_optimization_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
            "interactive_text_enabled": True,
            "responsive_web_text_conversations_enabled": False,
            "responsive_web_enhance_cards_enabled": False,
            "vibe_api_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "responsive_web_uc_gql_enabled": True,
            "view_counts_everywhere_api_enabled": True,
        }
        
        try:
            # Debug request
            cprint(f"Fetching likes for user ID: {user_id}", "blue")
            
            # Convert data to JSON strings first
            variables_data_encoded = json.dumps(variables_data)
            features_data_encoded = json.dumps(features_data)
            tweet_fields_encoded = json.dumps(["created_at", "full_text", "note_tweet"])
            
            response = requests.get(
                likes_url,
                params={
                    "variables": variables_data_encoded,
                    "features": features_data_encoded,
                    "tweet.fields": tweet_fields_encoded,
                },
                headers=self.twitter_headers
            )
            
            # Debug response
            cprint(f"Response status code: {response.status_code}", "blue")
            cprint(f"Request URL: {response.url[:200]}...", "blue")
            
            response.raise_for_status()
            data = response.json()
            
            # Debug response
            if 'errors' in data:
                cprint(f"API Errors: {json.dumps(data['errors'], indent=2)}", "red")
                return None
                
            # Extract tweets from response
            try:
                entries = data['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries']
                if not entries:
                    cprint("No entries found in timeline", "yellow")
                    return None
                
                tweets = []
                for entry in entries[:-1]:  # Skip last entry as it's the cursor
                    if 'content' not in entry:
                        continue
                        
                    content = entry['content']
                    if 'itemContent' not in content:
                        continue
                        
                    item_content = content['itemContent']
                    if 'tweet_results' not in item_content:
                        continue
                        
                    tweet_results = item_content['tweet_results']
                    if 'result' not in tweet_results:
                        continue
                        
                    tweet = self._extract_tweet_data(tweet_results['result'])
                    if tweet:
                        tweets.append(tweet)
                        
                return tweets
                
            except KeyError as e:
                cprint(f"Error parsing response structure: {str(e)}", "red")
                cprint(f"Response structure: {json.dumps(data, indent=2)[:500]}...", "yellow")
                return None
            
        except Exception as e:
            cprint(f"Error fetching user likes: {str(e)}", "red")
            if 'response' in locals():
                try:
                    cprint(f"Response: {response.text[:500]}...", "yellow")
                except:
                    pass
            return None

    def _extract_tweet_data(self, tweet_data):
        """Extract relevant data from a single tweet object returned by the Twitter API. This helper method parses the complex Twitter API response structure and extracts the most important tweet information into a clean, standardized format."""
        if not tweet_data:
            return None
            
        # Extract legacy data which contains most tweet information
        legacy = tweet_data.get("legacy", {})
        if not legacy:
            return None
            
        # Extract user information
        user_data = tweet_data.get("core", {}).get("user_results", {}).get("result", {}).get("legacy", {})
        
        # Extract media information
        media = []
        entities = legacy.get("entities", {})
        if "media" in entities:
            for m in entities["media"]:
                media.append({
                    "type": m.get("type"),
                    "url": m.get("media_url_https"),
                    "alt_text": m.get("ext_alt_text")
                })
                
        # Extract URLs
        urls = []
        if "urls" in entities:
            for u in entities["urls"]:
                urls.append({
                    "expanded_url": u.get("expanded_url"),
                    "display_url": u.get("display_url")
                })
                
        # Extract mentions
        mentions = []
        if "user_mentions" in entities:
            for mention in entities["user_mentions"]:
                mentions.append({
                    "username": mention.get("screen_name"),
                    "name": mention.get("name")
                })
                
        # Build clean tweet object
        tweet = {
            "id": legacy.get("id_str"),
            "text": legacy.get("full_text") or legacy.get("text"),
            "created_at": legacy.get("created_at"),
            "retweet_count": legacy.get("retweet_count", 0),
            "favorite_count": legacy.get("favorite_count", 0),
            "reply_count": legacy.get("reply_count", 0),
            "quote_count": legacy.get("quote_count", 0),
            "lang": legacy.get("lang"),
            "author": {
                "username": user_data.get("screen_name"),
                "name": user_data.get("name"),
                "followers_count": user_data.get("followers_count"),
                "following_count": user_data.get("friends_count"),
                "verified": user_data.get("verified", False)
            },
            "media": media if media else None,
            "urls": urls if urls else None,
            "mentions": mentions if mentions else None,
            "is_retweet": bool(legacy.get("retweeted_status_result")),
            "is_quote": bool(legacy.get("is_quote_status")),
            "conversation_id": legacy.get("conversation_id_str")
        }
        
        return tweet

    def _extract_tweets_from_user(self, data):
        """Extract and normalize tweets from a user timeline API response. This helper method processes the raw API response data from user timeline requests and converts it into a standardized tweet format for consistent handling throughout the application."""
        tweets = []
        try:
            # The actual response structure is simpler than documented
            results = data.get("results", [])
            for result in results:
                tweet = {
                    "id": result.get("tweet_id"),
                    "text": result.get("text"),
                    "created_at": result.get("creation_date"),
                    "retweet_count": result.get("retweet_count", 0),
                    "favorite_count": result.get("favorite_count", 0),
                    "reply_count": result.get("reply_count", 0),
                    "quote_count": result.get("quote_count", 0),
                    "lang": result.get("lang"),
                    "author": {
                        "username": result.get("user", {}).get("username"),
                        "name": result.get("user", {}).get("name"),
                        "followers_count": result.get("user", {}).get("followers_count", 0),
                        "following_count": result.get("user", {}).get("following_count", 0),
                        "verified": result.get("user", {}).get("verified", False)
                    },
                    "media": result.get("media"),
                    "urls": result.get("urls"),
                    "mentions": result.get("mentions"),
                    "is_retweet": result.get("text", "").startswith("RT @"),
                    "is_quote": bool(result.get("is_quote"))
                }
                tweets.append(tweet)
                        
        except Exception as e:
            cprint(f"Error extracting user tweets: {str(e)}", "red")
            
        return tweets

    def _extract_tweets_from_search(self, data):
        """Extract and normalize tweets from a search API response. This helper method processes the raw API response data from search requests and converts it into a standardized tweet format for consistent handling throughout the application."""
        tweets = []
        try:
            # The search endpoint has a different structure
            results = data.get("results", [])
            for result in results:
                tweet = {
                    "id": result.get("tweet_id"),
                    "text": result.get("text"),
                    "created_at": result.get("creation_date"),
                    "retweet_count": result.get("retweet_count", 0),
                    "favorite_count": result.get("favorite_count", 0),
                    "reply_count": result.get("reply_count", 0),
                    "quote_count": result.get("quote_count", 0),
                    "lang": result.get("lang"),
                    "author": {
                        "username": result.get("user", {}).get("username"),
                        "name": result.get("user", {}).get("name"),
                        "followers_count": result.get("user", {}).get("followers_count", 0),
                        "following_count": result.get("user", {}).get("following_count", 0),
                        "verified": result.get("user", {}).get("verified", False)
                    },
                    "media": result.get("media"),
                    "urls": result.get("urls"),
                    "mentions": result.get("mentions"),
                    "is_retweet": result.get("text", "").startswith("RT @"),
                    "is_quote": bool(result.get("is_quote"))
                }
                tweets.append(tweet)
                
        except Exception as e:
            cprint(f"Error extracting search results: {str(e)}", "red")
            
        return tweets

    def _extract_tweets_from_list(self, data):
        """Extract and normalize tweets from a Twitter list API response. This helper method processes the raw API response data from list requests and converts it into a standardized tweet format for consistent handling throughout the application."""
        tweets = []
        try:
            # The list endpoint has a similar structure to search
            results = data.get("tweets", [])
            for result in results:
                tweet = {
                    "id": result.get("tweet_id"),
                    "text": result.get("text"),
                    "created_at": result.get("creation_date"),
                    "retweet_count": result.get("retweet_count", 0),
                    "favorite_count": result.get("favorite_count", 0),
                    "reply_count": result.get("reply_count", 0),
                    "quote_count": result.get("quote_count", 0),
                    "lang": result.get("lang"),
                    "author": {
                        "username": result.get("user", {}).get("username"),
                        "name": result.get("user", {}).get("name"),
                        "followers_count": result.get("user", {}).get("followers_count", 0),
                        "following_count": result.get("user", {}).get("following_count", 0),
                        "verified": result.get("user", {}).get("verified", False)
                    },
                    "media": result.get("media"),
                    "urls": result.get("urls"),
                    "mentions": result.get("mentions"),
                    "is_retweet": result.get("text", "").startswith("RT @"),
                    "is_quote": bool(result.get("is_quote"))
                }
                tweets.append(tweet)
                
        except Exception as e:
            cprint(f"Error extracting list tweets: {str(e)}", "red")
            
        return tweets

def format_tweet(tweet):
    """Format a tweet for human-readable display in the terminal. This function takes a standardized tweet object and converts it into a well-structured, easy-to-read string format with all relevant tweet information including date, author, text content, media, URLs, and engagement metrics. The formatted output is designed for terminal display with clear section separators."""
    try:
        date = datetime.strptime(tweet.get("created_at"), "%a %b %d %H:%M:%S +0000 %Y").strftime('%Y-%m-%d %H:%M:%S')
    except:
        date = "Unknown date"
    
    # Build the formatted string
    output = [
        f"\nDate: {date}",
        f"Author: @{tweet['author']['username']} ({tweet['author']['name']})",
        f"{'✓ ' if tweet['author']['verified'] else ''}Followers: {tweet['author']['followers_count']}",
        f"\nText: {tweet.get('text', 'No text content')}",
    ]
    
    # Add media information if present
    if tweet.get('media'):
        output.append("\nMedia:")
        for m in tweet['media']:
            output.append(f"- {m['type']}: {m['url']}")
    
    # Add URL information if present
    if tweet.get('urls'):
        output.append("\nURLs:")
        for url in tweet['urls']:
            output.append(f"- {url['display_url']} ({url['expanded_url']})")
    
    # Add engagement metrics
    output.extend([
        f"\nEngagement:",
        f"- Retweets: {tweet.get('retweet_count', 0)}",
        f"- Likes: {tweet.get('favorite_count', 0)}",
        f"- Replies: {tweet.get('reply_count', 0)}",
        f"- Quotes: {tweet.get('quote_count', 0)}",
    ])
    
    # Add tweet metadata
    output.extend([
        f"\nTweet ID: {tweet.get('id', 'No ID available')}",
        f"Language: {tweet.get('lang', 'unknown')}",
        f"Type: {'Retweet' if tweet.get('is_retweet') else 'Quote Tweet' if tweet.get('is_quote') else 'Original Tweet'}",
        f"{'-' * 80}"
    ])
    
    return "\n".join(output)

def main():
    """Command-line interface for the Twitter API tool. This function parses command-line arguments and executes the appropriate Twitter API operations based on the specified action. 
    
    Available actions:
    - user-tweets: Get tweets from a specific user's timeline
    - search: Search for tweets based on keywords, hashtags, or phrases
    - list-tweets: Get tweets from a specific Twitter list
    - likes: Get tweets that a user has liked/favorited
    
    Each action requires specific parameters as documented in the help text.
    """
    parser = argparse.ArgumentParser(description='Twitter API Tool')
    parser.add_argument('action', choices=['user-tweets', 'search', 'list-tweets', 'likes'],
                      help='Action to perform')
    parser.add_argument('--username', help='Twitter username')
    parser.add_argument('--user-id', help='Twitter user ID (required for likes)')
    parser.add_argument('--query', help='Search query')
    parser.add_argument('--list-id', help='Twitter list ID')
    parser.add_argument('--section', choices=['top', 'latest', 'people', 'photos', 'videos'],
                      default='latest', help='Section to search in (for search only)')
    parser.add_argument('--limit', type=int, default=10, help='Number of results to return')
    parser.add_argument('--min-retweets', type=int, default=0, help='Minimum number of retweets')
    parser.add_argument('--min-likes', type=int, default=0, help='Minimum number of likes')
    parser.add_argument('--include-replies', action='store_true', help='Include reply tweets')
    parser.add_argument('--include-pinned', action='store_true', help='Include pinned tweets')
    parser.add_argument('--language', help='Filter by language (e.g., en)')
    parser.add_argument('--start-date', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='End date (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    if not os.getenv("RAPIDAPI_KEY"):
        cprint("Error: RAPIDAPI_KEY environment variable not set", "red")
        sys.exit(1)
    
    api = TwitterAPI()
    
    if args.action == 'user-tweets' and args.username:
        tweets = api.get_user_tweets(
            args.username,
            limit=args.limit,
            include_replies=args.include_replies,
            include_pinned=args.include_pinned
        )
        if tweets:
            cprint(f"\nTweets from @{args.username}:", "green")
            print("=" * 80)
            for tweet in tweets:
                print(format_tweet(tweet))
                
    elif args.action == 'search' and args.query:
        tweets = api.search_tweets(
            query=args.query,
            section=args.section,
            limit=args.limit,
            min_retweets=args.min_retweets,
            min_likes=args.min_likes,
            start_date=args.start_date,
            end_date=args.end_date,
            language=args.language
        )
        if tweets:
            cprint(f"\nSearch results for '{args.query}' in section '{args.section}':", "green")
            print("=" * 80)
            for tweet in tweets:
                print(format_tweet(tweet))
                
    elif args.action == 'list-tweets' and args.list_id:
        tweets = api.get_list_tweets(args.list_id, limit=args.limit)
        if tweets:
            cprint(f"\nTweets from list {args.list_id}:", "green")
            print("=" * 80)
            for tweet in tweets:
                print(format_tweet(tweet))
                
    elif args.action == 'likes' and args.user_id:
        tweets = api.get_user_likes(args.user_id, limit=args.limit)
        if tweets:
            cprint(f"\nLiked tweets for user {args.user_id}:", "green")
            print("=" * 80)
            for tweet in tweets:
                print(format_tweet(tweet))
    else:
        if args.action == 'likes' and not args.user_id:
            cprint("Error: --user-id is required for likes action", "red")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 