 import requests

# Initialize Notion API Token
API_TOKEN = "YOUR_NOTION_API_TOKEN_HERE"

# Base URL for Notion API
BASE_URL = "https://api.notion.com/v1/"

# Function to list databases in the workspace
def list_databases():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Notion-Version": "2021-08-16"
    }
    try:
        response = requests.get(f"{BASE_URL}databases", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

# Main program
if __name__ == "__main__":
    databases = list_databases()
    if databases:
        print(databases)
    else:
        print("Failed to fetch databases.")
