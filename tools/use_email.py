# tools/use_email.py
"""
This tool is used to send emails using the Hub's branded template. It is a simple tool that uses the ZAPIER_EMAIL_WEBHOOK_URL environment variable to send emails. It will create an email in my drafts for specified recipient/subject/body. 
Features: 
- Professional Hub branding with logo and styling
- Supports HTML formatting in content
- Automatic paragraph formatting with proper spacing
- Mobile-responsive design
- Social media links in footer
- Hub contact information automatically included
- Built-in markdown to HTML conversion (with --markdown flag)

IMPORTANT FORMATTING NOTES:
- By default, the tool does NOT convert markdown to HTML. You have two options:
  1. Provide properly formatted HTML in the content parameter
  2. Use the --markdown flag to automatically convert markdown content to HTML

- For simple text emails, plain text content will be automatically formatted with paragraph spacing.
- AVOID DUPLICATION: The template already includes:
  * The subject line at the top of the email
  * A signature block with "Regards, Chris Boden, Director, Peregian Digital Hub"
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
        <div style="font-family: Lora, Georgia, Times New Roman, serif; font-size: 16px; color: #2b2b2b; line-height: 1.6;">
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
                f'<font face="Lora, Georgia, Times New Roman, serif" size="5" color="#2b2b2b">'
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
    # Create a simpler, more traditional email template
    html = f'''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@400&display=swap" rel="stylesheet">
<title>{subject}</title>
</head>
<body bgcolor="#F9F6F2" style="margin: 0; padding: 0;">
<table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="#F9F6F2">
    <tr>
        <td align="center" valign="top">
            <table width="600" border="0" cellpadding="0" cellspacing="0">
                <!-- Header with images -->
                <tr>
                    <td bgcolor="#0f1328" style="padding: 10px 20px;">
                        <table width="100%" border="0" cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="50%" align="right" style="padding-right: 10px;">
                                    <img src="https://www.peregianhub.com.au/img/email/whale.png" width="250" alt="Whale" style="display: block; width: 100%; max-width: 250px;">
                                </td>
                                <td width="50%" align="left" style="padding-left: 10px;">
                                    <img src="https://www.peregianhub.com.au/img/email/tokenizer.png" width="250" alt="Tokenizer" style="display: block; width: 100%; max-width: 250px;">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <!-- Subject -->
                <tr>
                    <td style="padding: 40px 40px 20px 40px;">
                        <font face="Lora, Georgia, Times New Roman, serif" size="6" color="#2b2b2b">
                            {subject}
                        </font>
                    </td>
                </tr>
                <!-- Content -->
                <tr>
                    <td style="padding: 0 40px;">
                        {formatted_body}
                    </td>
                </tr>
                <!-- Signature -->
                <tr>
                    <td style="padding: 20px 40px;">
                        <font face="Lora, Georgia, Times New Roman, serif" size="5" color="#2b2b2b">
                            Regards<br><br>
                            Chris Boden<br>
                            Director, Peregian Digital Hub<br>
                            0421850424
                        </font>
                    </td>
                </tr>
                <!-- Logo and Footer -->
                <tr>
                    <td align="center" style="padding: 40px 0;">
                        <img src="https://www.peregianhub.com.au/img/email/logo.png" width="155" alt="Peregian Digital Hub" style="display: block; width: 155px;">
                        <table width="100%" border="0" cellpadding="20" cellspacing="0">
                            <tr>
                                <td align="center">
                                    <font face="Lora, Georgia, Times New Roman, serif" size="3" color="#2b2b2b">
                                        <a href="https://www.peregianhub.com.au/" style="color: #2b2b2b; text-decoration: underline;">peregianhub.com.au</a>
                                    </font>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <table border="0" cellpadding="5" cellspacing="0">
                                        <tr>
                                            <td><a href="https://facebook.com/peregianhub"><img src="https://www.peregianhub.com.au/img/email/fb.png" width="20" alt="Facebook"></a></td>
                                            <td><a href="https://linkedin.com/company/peregianhub"><img src="https://www.peregianhub.com.au/img/email/li.png" width="21" alt="LinkedIn"></a></td>
                                            <td><a href="https://www.youtube.com/@peregiandigitalhub4239"><img src="https://www.peregianhub.com.au/img/email/yt.png" width="20" alt="YouTube"></a></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <font face="Lora, Georgia, Times New Roman, serif" size="3" color="#2b2b2b">
                                        253-255 David Low Way<br>
                                        Peregian Beach QLD 4573, Australia
                                    </font>
                                </td>
                            </tr>
                        </table>
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
    parser = argparse.ArgumentParser(description='Send an HTML email using the Hub\'s branded template.')
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
        "description": "Send an HTML email using the Hub's branded template. Perfect for sending announcements, newsletters, or any communication that should have the Hub's professional look.",
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
                    "description": "Optional - Sender email address. Defaults to Hub's official email."
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