# tools/use_email.py
"""
This tool is used to send emails using a clean, professional boilerplate template. It is a simple tool that uses the ZAPIER_EMAIL_WEBHOOK_URL environment variable to send emails. It will create an email in my drafts for specified recipient/subject/body. 
Features: 
- Professional, clean design with modern styling
- Supports HTML formatting in content
- Automatic paragraph formatting with proper spacing
- Mobile-responsive design
- Built-in markdown to HTML conversion (with --markdown flag)

IMPORTANT FORMATTING NOTES:
- By default, the tool does NOT convert markdown to HTML. You have two options:
  1. Provide properly formatted HTML in the content parameter
  2. Use the --markdown flag to automatically convert markdown content to HTML

- For simple text emails, plain text content will be automatically formatted with paragraph spacing.
- AVOID DUPLICATION: The template already includes:
  * The subject line at the top of the email
  * A signature block with "Regards, Tony Le"
  * Do NOT repeat these elements in your content

- HANDLING MULTILINE CONTENT:
  * For multiline content, always use the file redirection method: --content "$(cat your_file.md)"
  * DO NOT pass multiline content directly as it will cause command parsing errors
  * If you must pass content directly, use \n to represent newlines in a single line string

- Example workflows:
  1. HTML content:
     python3 tools/use_email.py --to recipient@example.com --subject "My Subject" --content "$(cat notes/my_email_content.html)"
  
  2. Markdown content:
     python3 tools/use_email.py --to recipient@example.com --subject "My Subject" --content "$(cat notes/my_email_content.md)" --markdown

  3. Direct text content:
     python3 tools/use_email.py --to recipient@example.com --subject "My Subject" --content "This is a simple email message."

"""
import os
import requests
import argparse
import json
import re
from typing import List, Optional, Union
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to import markdown module, but make it optional
try:
    import markdown
    MARKDOWN_AVAILABLE = True
except ImportError:
    MARKDOWN_AVAILABLE = False

def convert_markdown_to_html(md_content):
    """Convert markdown content to HTML, removing subject and signature to prevent duplication."""
    if not MARKDOWN_AVAILABLE:
        raise ImportError("The markdown package is not installed. Install it with 'pip install markdown'")
    
    # Configure markdown extensions
    extensions = [
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
    ]
    
    # Remove the first heading (usually the title) to prevent duplication with the subject
    # This regex looks for a level 1-3 heading at the start of the content
    md_content = re.sub(r'^#{1,3}\s+.*?\n', '', md_content, count=1, flags=re.MULTILINE)
    
    # Remove signature section if present (common markdown patterns for signatures)
    signature_patterns = [
        r'\n\s*Regards,.*?$',  # Common signature starting with "Regards,"
        r'\n\s*Sincerely,.*?$',  # Common signature starting with "Sincerely,"
        r'\n\s*Best,.*?$',  # Common signature starting with "Best,"
        r'\n\s*---+\s*\n.*?$'  # Markdown horizontal rule often used before signatures
    ]
    
    for pattern in signature_patterns:
        md_content = re.sub(pattern, '', md_content, flags=re.DOTALL)
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=extensions)
    
    return html_content

def format_body_content(content):
    # Check if content appears to be HTML
    if "<html" in content.lower() or "<body" in content.lower() or "<div" in content.lower() or "<p" in content.lower() or "<h" in content.lower():
        # If it's already HTML, wrap it in a container for consistent styling
        return f'''
        <table width="100%" border="0" cellpadding="0" cellspacing="0"><tr><td>
        <div style="font-family: 'Open Sans', Arial, sans-serif; font-size: 16px; color: #333333; line-height: 1.6;">
        {content}
        </div>
        </td></tr></table>
        '''
    
    # Otherwise, format as paragraphs
    paragraphs = content.split('\n\n')
    formatted_paragraphs = []
    for para in paragraphs:
        if para.strip():
            # Use traditional email-safe markup with font tags and basic attributes
            formatted = (
                f'<table width="100%" border="0" cellpadding="0" cellspacing="0"><tr><td>'
                f'<font face="Open Sans, Arial, sans-serif" size="4" color="#333333">'
                f'{para}'
                f'</font>'
                f'</td></tr></table>'
                f'<table width="100%" border="0" cellpadding="0" cellspacing="0" style="height:20px"><tr><td>&nbsp;</td></tr></table>'
            )
            formatted_paragraphs.append(formatted)
    return '\n'.join(formatted_paragraphs)

def apply_template(subject: str, body_content: str) -> str:
    # If content appears to be complete HTML document, use it directly
    if "<html" in body_content.lower() and "<body" in body_content.lower():
        return body_content
        
    formatted_body = format_body_content(body_content)
    # Create a clean, professional email template
    html = f'''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
<title>{subject}</title>
<style>
  body {{ font-family: 'Open Sans', Arial, sans-serif; line-height: 1.6; color: #333333; margin: 0; padding: 0; }}
  .container {{ max-width: 600px; margin: 0 auto; }}
  .header {{ background-color: #f8f9fa; padding: 20px; text-align: center; border-bottom: 3px solid #4a90e2; }}
  .content {{ padding: 30px; background-color: #ffffff; }}
  .footer {{ background-color: #f8f9fa; padding: 20px; text-align: center; font-size: 14px; color: #666666; }}
  h1 {{ color: #4a90e2; margin-top: 0; }}
  a {{ color: #4a90e2; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .signature {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #eeeeee; }}
</style>
</head>
<body bgcolor="#f4f4f4" style="margin: 0; padding: 0;">
<table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="#f4f4f4">
    <tr>
        <td align="center" valign="top" style="padding: 20px 0;">
            <table class="container" width="600" border="0" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="border-radius: 5px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                <!-- Header -->
                <tr>
                    <td class="header" style="padding: 20px; text-align: center; background-color: #f8f9fa; border-bottom: 3px solid #4a90e2; border-radius: 5px 5px 0 0;">
                        <h1 style="color: #4a90e2; margin: 0; font-size: 24px; font-weight: 600;">{subject}</h1>
                    </td>
                </tr>
                <!-- Content -->
                <tr>
                    <td class="content" style="padding: 30px; background-color: #ffffff;">
                        {formatted_body}
                    </td>
                </tr>
                <!-- Signature -->
                <tr>
                    <td class="signature" style="padding: 0 30px 20px 30px;">
                        <table width="100%" border="0" cellpadding="0" cellspacing="0" style="border-top: 1px solid #eeeeee; padding-top: 20px; margin-top: 20px;">
                            <tr>
                                <td>
                                    <p style="margin: 0; font-size: 16px; color: #333333;">
                                        Regards,<br><br>
                                        Tony Le<br>
                                        0480144280
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <!-- Footer -->
                <tr>
                    <td class="footer" style="padding: 20px; text-align: center; background-color: #f8f9fa; border-radius: 0 0 5px 5px; font-size: 14px; color: #666666;">
                        <p style="margin: 0;">This email was sent using an automated system.</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
</body>
</html>
'''
    return html

def execute(
    to: Optional[List[str]], 
    subject: str, 
    html_body: str,
    body: Optional[str] = None,
    cc: Optional[List[str]] = None, 
    bcc: Optional[List[str]] = None, 
    from_email: Optional[str] = 'chris.boden@noosa.qld.gov.au'
):
    webhook_url = os.getenv('ZAPIER_EMAIL_WEBHOOK_URL')
    if not webhook_url:
        raise ValueError("ZAPIER_EMAIL_WEBHOOK_URL is not set in environment variables")

    final_html = apply_template(subject, html_body)
    payload = {
        'to': to,
        'subject': subject,
        'html_body': final_html
    }

    if body:
        payload['body'] = body
    else:
        payload['body'] = html_body

    if cc:
        payload['cc'] = cc
    if bcc:
        payload['bcc'] = bcc
    if from_email:
        payload['from_email'] = from_email

    try:
        response = requests.post(
            webhook_url, 
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200:
            return f"Successfully sent email: {subject}"
        else:
            return f"Failed to send email: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error sending email: {str(e)}"

def send_email(
    to: Union[str, List[str]], 
    subject: str, 
    content: str,
    cc: Optional[Union[str, List[str]]] = None,
    bcc: Optional[Union[str, List[str]]] = None,
    from_email: Optional[str] = None,
    is_markdown: bool = False
):
    to_list = [to] if isinstance(to, str) else to
    cc_list = [cc] if cc and isinstance(cc, str) else cc
    bcc_list = [bcc] if bcc and isinstance(bcc, str) else bcc

    try:
        # Check if content is a file path and read it if it exists
        if os.path.isfile(content):
            try:
                with open(content, 'r') as file:
                    content = file.read()
            except Exception as e:
                return f"Error reading file {content}: {str(e)}"
        
        # Convert markdown to HTML if requested
        if is_markdown:
            if not MARKDOWN_AVAILABLE:
                return "Error: Markdown conversion requested but markdown package is not installed. Install it with 'pip install markdown'"
            content = convert_markdown_to_html(content)
        
        return execute(
            to=to_list,
            subject=subject,
            html_body=content,
            cc=cc_list,
            bcc=bcc_list,
            from_email=from_email
        )
    except Exception as e:
        return f"Error in send_email: {str(e)}"

def parse_list_arg(arg: str) -> List[str]:
    """Parse a comma-separated string into a list of strings."""
    if not arg:
        return None
    return [x.strip() for x in arg.split(',') if x.strip()]

def main():
    """CLI entry point for the email tool."""
    parser = argparse.ArgumentParser(description='Send an HTML email using a clean, professional boilerplate template.')
    parser.add_argument('--to', required=True, help='Comma-separated list of recipient email addresses')
    parser.add_argument('--subject', required=True, help='Subject line of the email')
    parser.add_argument('--content', required=True, help='Content of the email')
    parser.add_argument('--cc', help='Comma-separated list of CC recipients')
    parser.add_argument('--bcc', help='Comma-separated list of BCC recipients')
    parser.add_argument('--from-email', help='Sender email address')
    parser.add_argument('--markdown', action='store_true', help='Treat content as markdown and convert to HTML')
    
    args = parser.parse_args()
    
    result = send_email(
        to=parse_list_arg(args.to),
        subject=args.subject,
        content=args.content,
        cc=parse_list_arg(args.cc),
        bcc=parse_list_arg(args.bcc),
        from_email=args.from_email,
        is_markdown=args.markdown
    )
    print(result)

if __name__ == '__main__':
    main()

TOOL_METADATA = {
    "type": "function",
    "function": {
        "name": "use_email",
        "description": "Send an HTML email using a clean, professional boilerplate template. Perfect for sending announcements, newsletters, or any professional communication.",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "oneOf": [
                        {"type": "string"},
                        {"type": "array", "items": {"type": "string"}}
                    ],
                    "description": "Single email address or list of recipient email addresses"
                },
                "subject": {
                    "type": "string",
                    "description": "Subject line of the email"
                },
                "content": {
                    "type": "string",
                    "description": "The main content of the email. For simple text, plain content will be formatted automatically. For complex formatting (headings, links, lists), provide properly formatted HTML - the tool does NOT convert markdown to HTML by default. IMPORTANT: Do NOT include the subject line or signature in your content as these are automatically added by the template."
                },
                "cc": {
                    "oneOf": [
                        {"type": "string"},
                        {"type": "array", "items": {"type": "string"}}
                    ],
                    "description": "Optional - Single email address or list of CC recipients"
                },
                "bcc": {
                    "oneOf": [
                        {"type": "string"},
                        {"type": "array", "items": {"type": "string"}}
                    ],
                    "description": "Optional - Single email address or list of BCC recipients"
                },
                "from_email": {
                    "type": "string",
                    "description": "Optional - Sender email address. Defaults to official email."
                },
                "is_markdown": {
                    "type": "boolean",
                    "description": "Optional - Set to true if the content is in markdown format and should be converted to HTML. Automatically removes first heading and signature section to prevent duplication.",
                    "default": False
                }
            },
            "required": ["to", "subject", "content"]
        }
    }
}