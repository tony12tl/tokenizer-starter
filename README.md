# Tokenizer Starter Repository

A starter repository for members of the Peregian Digital Hub's Tokenizer program. This repository helps you get up and running with your first Agent workflows.

## About the Tokenizer Program

The Tokenizer program at Peregian Digital Hub provides tools and resources for building AI-powered agent workflows. This starter repository includes a sample email templating tool to demonstrate how to create useful agent tools.

## Included Tools

### Email Templating Tool

A simple Python tool for sending emails with a clean, professional boilerplate template. This tool uses the Zapier Email Webhook to create draft emails with proper formatting.

#### Features

- Professional, clean design with modern styling
- Supports HTML formatting in content
- Automatic paragraph formatting with proper spacing
- Mobile-responsive design
- Built-in markdown to HTML conversion (with --markdown flag)

#### Usage

```bash
python3 tools/use_email.py --to recipient@example.com --subject "My Subject" --content "This is a simple email message."
```

#### Options

- `--to`: Comma-separated list of recipient email addresses (required)
- `--subject`: Subject line of the email (required)
- `--content`: Content of the email (required)
- `--cc`: Comma-separated list of CC recipients
- `--bcc`: Comma-separated list of BCC recipients
- `--from-email`: Sender email address
- `--markdown`: Treat content as markdown and convert to HTML

#### Example Workflows

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

## Getting Started

1. Clone this repository
2. Set the `ZAPIER_EMAIL_WEBHOOK_URL` environment variable with your Zapier webhook URL
3. Install required dependencies: `pip install -r requirements.txt`

## Building Your Own Tools

This repository serves as a starting point for creating your own agent tools. Follow these steps:

1. Explore the existing tools in the `/tools` directory
2. Create new tools following the same pattern
3. Test your tools with various inputs
4. Integrate your tools into your agent workflows

## Requirements

- Python 3.6+
- Required Python packages are listed in `requirements.txt` 