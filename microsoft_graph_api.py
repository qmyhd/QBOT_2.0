 from requests_oauthlib import OAuth2Session
import json

# Microsoft Graph API endpoints
AUTHORIZATION_BASE_URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
TOKEN_URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
REDIRECT_URI = 'YOUR_REDIRECT_URI'  # Replace with your redirect URI

# App registration details
CLIENT_ID = 'YOUR_CLIENT_ID'  # Replace with your client ID
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # Replace with your client secret

# Initialize OAuth2 session
oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=['User.Read', 'Mail.ReadWrite', 'Calendars.ReadWrite'])

# Fetch authorization URL and state
authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)

# Open authorization URL, authenticate and authorize the app
print(f"Please visit this URL to authorize the app: {authorization_url}")

# Get the authorization response URL from the user
authorization_response = input("Enter the full callback URL: ")

# Fetch the access token
token = oauth.fetch_token(TOKEN_URL, authorization_response=authorization_response, client_secret=CLIENT_SECRET)

# Fetch emails
def fetch_emails():
    response = oauth.get('https://graph.microsoft.com/v1.0/me/messages')
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Send email
def send_email(subject, recipients, body):
    payload = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": body
            },
            "toRecipients": [{"emailAddress": {"address": recipient}} for recipient in recipients]
        }
    }
    response = oauth.post('https://graph.microsoft.com/v1.0/me/sendMail', json=payload)
    return response.status_code == 202

# Create calendar event
def create_calendar_event(subject, start, end):
    payload = {
        "subject": subject,
        "start": {
            "dateTime": start,
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": end,
            "timeZone": "UTC"
        }
    }
    response = oauth.post('https://graph.microsoft.com/v1.0/me/events', json=payload)
    if response.status_code == 201:
        return response.json()
    else:
        return None

# Main program
if __name__ == "__main__":
    # Fetch emails
    emails = fetch_emails()
    if emails:
        print("Fetched emails:", emails)
    else:
        print("Failed to fetch emails.")

    # Send email
    is_sent = send_email("Test Subject", ["recipient@example.com"], "Test Body")
    if is_sent:
        print("Email sent successfully.")
    else:
        print("Failed to send email.")

    # Create calendar event
    event = create_calendar_event("Test Event", "2022-12-31T12:00:00", "2022-12-31T13:00:00")
    if event:
        print("Event created:", event)
    else:
        print("Failed to create event.")

