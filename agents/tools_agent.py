#!/usr/bin/env python3
"""
agents/tools_agent.py - A tool to determine optimal tool steps for a given user request.

This script uses an LLM to analyze the available tools in manifest.json and recommend a plan of action to achieve the user's goal.
"""

import os
import json
import argparse
import sys
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Get the root directory (two levels up from the script directory since we're in agents/)
ROOT_DIR = Path(__file__).parent.parent
# Load environment variables from .env file in root
load_dotenv(ROOT_DIR / '.env')

def load_file(file_path):
    """Load a file's contents."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        sys.exit(1)

def get_about_me():
    """Get the about_me.md content if it exists."""
    about_me_paths = [
        ROOT_DIR / "about_me.md",
        ROOT_DIR / "instructions" / "about_me.md",
        ROOT_DIR / ".cursor" / "about_me.md"
    ]
    
    for path in about_me_paths:
        if path.exists():
            return load_file(path)
    
    # If no about_me.md is found, return a basic description
    return "The user is Chris Boden who runs the Peregian Digital Hub, an environment for people building technology companies, located in Peregian Beach - a suburb of Noosa."

def get_manifest():
    """Get the manifest.json content."""
    manifest_path = ROOT_DIR / "tools" / "manifest.json"
    return load_file(manifest_path)

def ask_llm(user_message):
    """
    Ask the LLM to determine the optimal tool steps for the user's request.
    """
    api_base_url = os.getenv('API_BASE_URL')
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_base_url or not api_key:
        print("Error: API_BASE_URL or OPENROUTER_API_KEY environment variables not set.")
        print(f"API_BASE_URL: {api_base_url}")
        print(f"OPENROUTER_API_KEY: {'*' * len(api_key) if api_key else 'Not set'}")
        sys.exit(1)
    
    client = OpenAI(
        base_url=api_base_url,
        api_key=api_key
    )
    
    about_me = get_about_me()
    manifest = get_manifest()
    
    system_message = f"""You are an AI agent that is brilliant at determining a plan of action to achieve a given user goal, by using a given set of tools. You respond with a tool calling plan, in json.

Here is some background on the user:

{about_me}

Below is a manifest detailing the tools you have available.

{manifest}

Your response should be a valid JSON object which outlines the plan for which tools need to be called, with what arguments and in what order. Include only the tools that are absolutely necessary to achieve the user's goal.

The JSON MUST follow this exact schema:
{{
  "plan": {{
    "summary": "Brief summary of the overall plan",
    "steps": [
      {{
        "tool": "tools/filename.py",
        "command": "command_name",
        "arguments": {{ "arg1": "value1", "arg2": "value2" }},
        "purpose": "Explanation of why this step is necessary"
      }}
    ]
  }}
}}

IMPORTANT: Your response must be ONLY valid JSON that can be parsed with json.loads() - no other text before or after.

For each step:
1. "tool" should be the pathed filename of the tool (e.g., "tools/use_twitter.py")
2. "command" should be the specific command to run (e.g., "likes")
3. "arguments" should be an object containing all required parameters for the command. In the case where the arguments for a subsequent step are the output of a previous step, you should note that the output of the previous step is the value for the argument.
4. "purpose" should explain why this step is necessary

Be specific and detailed in your plan. Include all necessary steps to complete the user's request.
"""
    
    user_prompt = f"The user has asked the following: {user_message}"
    
    try:
        response = client.chat.completions.create(
            model="google/gemini-2.0-flash-lite-001",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ],
            response_format={
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "plan": {
                            "type": "object",
                            "properties": {
                                "summary": {
                                    "type": "string",
                                    "description": "Brief summary of the overall plan"
                                },
                                "steps": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "tool": {
                                                "type": "string",
                                                "description": "The pathed filename of the tool (e.g., tools/use_twitter.py)"
                                            },
                                            "command": {
                                                "type": "string",
                                                "description": "The specific command to run"
                                            },
                                            "arguments": {
                                                "type": "object",
                                                "description": "Object containing all required parameters for the command"
                                            },
                                            "purpose": {
                                                "type": "string",
                                                "description": "Explanation of why this step is necessary"
                                            }
                                        },
                                        "required": ["tool", "command", "arguments", "purpose"]
                                    }
                                }
                            },
                            "required": ["summary", "steps"]
                        }
                    },
                    "required": ["plan"]
                }
            }
        )
        
        # Extract and parse the JSON response
        if not response.choices:
            raise ValueError("No response received from LLM")
            
        content = response.choices[0].message.content
        if not content:
            raise ValueError("Empty response received from LLM")
            
        print("\nDEBUG: Raw LLM Response:")
        print("=" * 50)
        print(content)
        print("=" * 50)
        print("\n")
            
        # Clean the content by removing markdown code block formatting if present
        if content.startswith("```"):
            # Find the first and last ``` and extract content between them
            start_idx = content.find("\n", content.find("```")) + 1
            end_idx = content.rfind("```")
            if end_idx > start_idx:
                content = content[start_idx:end_idx].strip()
                print("\nDEBUG: Cleaned JSON:")
                print("=" * 50)
                print(content)
                print("=" * 50)
                print("\n")
            
        # Parse and validate the JSON response
        try:
            parsed_content = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"\nError: Failed to parse JSON. Error location: line {e.lineno}, column {e.colno}")
            print(f"Error message: {str(e)}")
            raise
            
        if "plan" not in parsed_content:
            raise ValueError("Response missing required 'plan' field")
            
        # Format the JSON with indentation for better readability
        formatted_json = json.dumps(parsed_content, indent=2)
        return parsed_content, formatted_json
            
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON response from LLM: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Determine optimal tool steps for a user request")
    parser.add_argument("user_message", help="The user's request")
    parser.add_argument("--execute", action="store_true", help="Execute the recommended steps (deprecated, will be removed)")
    args = parser.parse_args()
    
    _, formatted_json = ask_llm(args.user_message)
    print(formatted_json)
    
    if args.execute:
        print("\nWARNING: The --execute flag is deprecated and will be removed in a future version.", file=sys.stderr)
        print("The Cursor agent should handle the execution of the plan instead.", file=sys.stderr)

if __name__ == "__main__":
    main() 