import requests

# Initialize GitHub API Token and Base URL
TOKEN = "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"
BASE_URL = "https://api.github.com"

# Function to list repositories of a given username
def list_repositories(qmyhd):
    headers = {"Authorization": f"token {TOKEN}"}
    try:
        response = requests.get(f"{BASE_URL}/users/{username}/repos", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to list repositories. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

# Function to create a new repository
def create_repository(repo_name):
    headers = {"Authorization": f"token {TOKEN}"}
    payload = {"name": repo_name}
    try:
        response = requests.post(f"{BASE_URL}/user/repos", headers=headers, json=payload)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: Unable to create repository. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None