import os
import json
import hashlib
import time
from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError, RateLimitError

load_dotenv()

# Use keys from .env
API_BASE_URL = os.getenv("API_BASE_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "google/gemini-2.0-flash-lite-001"

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=OPENROUTER_API_KEY
)

# Get the script directory and workspace directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)

# Define paths relative to workspace
MANIFEST_FILE = os.path.join(WORKSPACE_DIR, "tools/manifest.json")
TOOLS_DIR = SCRIPT_DIR  # The tools directory is where this script is located

def calculate_file_hash(file_path):
    """Compute a SHA256 hash of the file's contents."""
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def collect_tool_files(directory=TOOLS_DIR):
    """Collect all Python tool files from the directory."""
    tool_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename != "__init__.py" and filename != "manifest.py":
            tool_files.append(os.path.join(directory, filename))
    return tool_files

def load_existing_manifest(manifest_file=MANIFEST_FILE):
    """Load the existing manifest from disk, or return a default structure."""
    if os.path.exists(manifest_file):
        with open(manifest_file, "r") as f:
            return json.load(f)
    return {"tools": {}}

def call_llm_api(prompt, max_retries=3, retry_delay=2):
    """
    Call the OpenRouter API (via OpenAI client) with the provided prompt.
    Uses structured outputs to ensure the response is valid JSON.
    
    Args:
        prompt (str): The prompt to send to the LLM
        max_retries (int): Maximum number of retries on failure
        retry_delay (int): Seconds to wait between retries
        
    Returns:
        str: The LLM's response content
    """
    retries = 0
    while retries <= max_retries:
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                response_format={
                    "type": "json_object",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "commands": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string",
                                            "description": "File name of the tool file, eg 'tools/use_email.py'"
                                        },
                                        "description": {
                                            "type": "string",
                                            "description": "Description of what the command does"
                                        },
                                        "usage": {
                                            "type": "string",
                                            "description": "Usage pattern for the command"
                                        },
                                        "parameters": {
                                            "type": "array",
                                            "description": "List of parameters for the command",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "name": {
                                                        "type": "string",
                                                        "description": "Name of the parameter"
                                                    },
                                                    "description": {
                                                        "type": "string",
                                                        "description": "Description of the parameter"
                                                    },
                                                    "type": {
                                                        "type": "string",
                                                        "description": "Data type of the parameter (string, integer, boolean, etc.)"
                                                    },
                                                    "required": {
                                                        "type": "boolean",
                                                        "description": "Whether the parameter is required"
                                                    },
                                                    "default": {
                                                        "description": "Default value for the parameter if not provided"
                                                    }
                                                },
                                                "required": ["name", "description"]
                                            }
                                        }
                                    },
                                    "required": ["name", "description", "usage"]
                                }
                            }
                        },
                        "required": ["commands"]
                    }
                }
            )
            return response.choices[0].message.content
        except RateLimitError:
            retries += 1
            if retries <= max_retries:
                print(f"Rate limit exceeded. Retrying in {retry_delay} seconds... (Attempt {retries}/{max_retries})")
                time.sleep(retry_delay)
                # Increase delay for next retry (exponential backoff)
                retry_delay *= 2
            else:
                print("Max retries exceeded. Could not complete API call due to rate limits.")
                raise
        except APIError as e:
            retries += 1
            if retries <= max_retries:
                print(f"API error: {e}. Retrying in {retry_delay} seconds... (Attempt {retries}/{max_retries})")
                time.sleep(retry_delay)
                # Increase delay for next retry (exponential backoff)
                retry_delay *= 2
            else:
                print(f"Max retries exceeded. API error: {e}")
                raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

def update_manifest_for_file(file_path, existing_entry=None):
    """
    For a given tool file, use the LLM to generate a manifest snippet.
    Uses structured outputs to ensure the response is valid JSON.
    
    Args:
        file_path (str): Path to the tool file
        existing_entry (dict, optional): Existing manifest entry for this file
        
    Returns:
        dict: The updated manifest entry for this file
    """
    with open(file_path, "r") as f:
        file_content = f.read()
    filename = os.path.basename(file_path)
    prompt = f"""
Your job is to create a tool manifest that accurately captures the CLI commands exposed by the following code file. The manifest contains multiple tool metadatas that will be used by an AI agent (referred to as 'the agent' to understand what tools it has available to it and how to use them.

CODE FILE: {filename}
==============
{file_content}
==============

Analyze the code and identify all CLI commands it exposes. For each command, provide:
1. The command name
2. A clear description of what it does - remember that this manifest will be read by an AI agent with the purpose of informing it about the tools it has available to it, so it is important to that the description explains how and when the tool should be used. If the command description is not detailed enough, use information from the docstring for the tool. Do not use the term 'you' to refer to the agent - intead use the third person term 'the agent' when referring to the agent that will be calling the tools. Remember that the agent takes instructions from a user and works on their behalf - refer to that person as 'the user'. 
3. Usage pattern showing how to invoke it
4. Any parameters it accepts

Your response should be a JSON object with the following structure:
{{
  "commands": [
    {{
      "name": "tools/file_name.py",
      "description": "Description of what the command does",
      "usage": "Usage pattern showing how to invoke it",
      "parameters": [
        {{
          "name": "parameter_name",
          "description": "Description of the parameter",
          "type": "Data type (string, integer, boolean, etc.)",
          "required": true/false,
          "default": "Default value if any"
        }}
      ]
    }}
  ]
}}

Return only valid JSON that matches this structure.
    """
    llm_response = call_llm_api(prompt)
    
    # Clean up the response if it's wrapped in a code block
    if llm_response.strip().startswith("```") and llm_response.strip().endswith("```"):
        # Extract content between the code block markers
        lines = llm_response.strip().split('\n')
        if len(lines) > 2:  # At least 3 lines (opening marker, content, closing marker)
            # Remove the first line (opening marker) and the last line (closing marker)
            llm_response = '\n'.join(lines[1:-1])
    
    # Also handle the case where it starts with ```json
    if llm_response.strip().startswith("```json"):
        lines = llm_response.strip().split('\n')
        if len(lines) > 2:  # At least 3 lines
            # Remove the first line (```json) and the last line (```)
            llm_response = '\n'.join(lines[1:-1])
    
    try:
        # With structured outputs, the response should already be valid JSON
        new_manifest_entry = json.loads(llm_response)
        
        # Handle the case where the response is wrapped in a "tool_manifest" object
        if "tool_manifest" in new_manifest_entry and "commands" in new_manifest_entry["tool_manifest"]:
            return new_manifest_entry["tool_manifest"]
        
        return new_manifest_entry
    except json.JSONDecodeError as e:
        print(f"Error decoding LLM response for {file_path}: {e}")
        print(f"Raw response: {llm_response}")
        return existing_entry if existing_entry else None

def differential_manifest_update():
    """
    Load the existing manifest and update it only for files that have changed.
    New or modified files are processed via the LLM; removed files are deleted from the manifest.
    """
    existing_manifest = load_existing_manifest()
    updated_manifest = existing_manifest.copy()
    if "tools" not in updated_manifest:
        updated_manifest["tools"] = {}
    
    tool_files = collect_tool_files()
    print(f"Found {len(tool_files)} tool files to process")
    
    for file_path in tool_files:
        filename = os.path.basename(file_path)
        file_hash = calculate_file_hash(file_path)
        
        # If the file hasn't changed, keep its manifest entry.
        if filename in updated_manifest["tools"]:
            if updated_manifest["tools"][filename].get("hash") == file_hash:
                print(f"Skipping unchanged file: {filename}")
                continue
        
        print(f"Processing file: {filename}")
        # File is new or has changed – update its manifest entry.
        new_entry = update_manifest_for_file(file_path, updated_manifest["tools"].get(filename))
        if new_entry is not None:
            updated_manifest["tools"][filename] = {
                "hash": file_hash,
                "commands": new_entry.get("commands", [])
            }
        else:
            print(f"Warning: Could not generate manifest entry for {filename}")
    
    # Remove entries for files that no longer exist.
    existing_files = {os.path.basename(fp) for fp in tool_files}
    for filename in list(updated_manifest["tools"].keys()):
        if filename not in existing_files:
            print(f"Removing entry for deleted file: {filename}")
            del updated_manifest["tools"][filename]
    
    with open(MANIFEST_FILE, "w") as f:
        json.dump(updated_manifest, f, indent=4)
    print(f"Manifest updated differentially and saved to {MANIFEST_FILE}")

if __name__ == "__main__":
    differential_manifest_update()