import requests

# Initialize Glassdoor API credentials
API_KEY = "YOUR_API_KEY_HERE"
PARTNER_ID = "YOUR_PARTNER_ID_HERE"

# Base URL for Glassdoor API
BASE_URL = "http://api.glassdoor.com/api/api.htm"

# Function to fetch company reviews
def fetch_company_reviews(company_name, num_results=10):
    params = {
        "t.p": PARTNER_ID,
        "t.k": API_KEY,
        "userip": "0.0.0.0",
        "useragent": "Mozilla/5.0",
        "format": "json",
        "v": "1",
        "action": "employers",
        "q": company_name,
        "ps": num_results
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

# Function to fetch job market research, salary estimates can be added similarly
# ...

if __name__ == "__main__":
    company_name = "Google"
    reviews = fetch_company_reviews(company_name)
    if reviews:
        print(reviews)
    else:
        print("Failed to fetch reviews.") 
