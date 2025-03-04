# Email Templating Tool

A simple Python tool for sending emails with a clean, professional boilerplate template. This tool uses the Zapier Email Webhook to create draft emails with proper formatting.

## Features

- Professional, clean design with modern styling
- Supports HTML formatting in content
- Automatic paragraph formatting with proper spacing
- Mobile-responsive design
- Built-in markdown to HTML conversion (with --markdown flag)

## Usage

```bash
python3 tools/use_email.py --to recipient@example.com --subject "My Subject" --content "This is a simple email message."
```

### Options

- `--to`: Comma-separated list of recipient email addresses (required)
- `--subject`: Subject line of the email (required)
- `--content`: Content of the email (required)
- `--cc`: Comma-separated list of CC recipients
- `--bcc`: Comma-separated list of BCC recipients
- `--from-email`: Sender email address
- `--markdown`: Treat content as markdown and convert to HTML

### Example Workflows

1. HTML content:
   ```bash
   python3 tools/use_email.py --to recipient@example.com --subject "My Subject" --content "$(cat notes/my_email_content.html)"
   ```

2. Markdown content:
   ```bash
   python3 tools/use_email.py --to recipient@example.com --subject "My Subject" --content "$(cat notes/my_email_content.md)" --markdown
   ```

3. Direct text content:
   ```bash
   python3 tools/use_email.py --to recipient@example.com --subject "My Subject" --content "This is a simple email message."
   ```

## Setup

1. Clone this repository
2. Set the `ZAPIER_EMAIL_WEBHOOK_URL` environment variable with your Zapier webhook URL
3. Install required dependencies: `pip install requests markdown python-dotenv`

## Requirements

- Python 3.6+
- `requests` library
- `markdown` library (optional, for markdown conversion)
- `python-dotenv` library (for environment variables) 