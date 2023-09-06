import requests
import json

CLIENT_ID = "772anfq9wksxnu"
CLIENT_SECRET = "Fi9s8iMjAksTbWFP"
ACCESS_TOKEN = "AQUlMErw4FpJlSeLRSwsaAroEwV8Ep_yXxQ9BJI1vskSXbttpVOH8EPZIqkFXrxowox7ZD9pACTLrmt9lcHvCd8WfTyjJSVggoAMMux1VOGFIS4C6tfRUeGFs-AVUNs8nr_t8a19EGu9PnhcyIXP3Xr0ZzO5ksdsd5k4UagHMjZ5CR8oh8ZHr1apUGqgxHWKS5vPCZiJdfrW-jkWxcvL3dEWw48zi58kQsd6_iyTAmRwuYQasBazG2qpZu1RCZwuO_1p8pfCKhRHKrdbiH8s5Jm-WGv0qrlx6Dkp2FOBa_o9DF6UhWCnBJhBi6uKWPgeASYfhGrFto7dCzErnZrLNLEsGGBprA"  # Replace with your actual access token

BASE_URL = "https://api.linkedin.com/v2/"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}

def create_text_share(author_urn, text):
    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(f"{BASE_URL}ugcPosts", headers=headers, data=json.dumps(payload))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")  # Print the response body for debugging

    if response.status_code == 201:
        return response.headers.get("X-RestLi-Id")
    else:
        return None

if __name__ == "__main__":
    author_urn = "urn:li:person:your_person_urn_here"  # Replace with your Person URN
    text = "Hello World! This is my first Share on LinkedIn!"

    post_id = create_text_share(author_urn, text)
    if post_id:
        print(f"Successfully created post with ID: {post_id}")
    else:
        print("Failed to create post")
 
 
#######
import requests
import json

ACCESS_TOKEN = "AQUlMErw4FpJlSeLRSwsaAroEwV8Ep_yXxQ9BJI1vskSXbttpVOH8EPZIqkFXrxowox7ZD9pACTLrmt9lcHvCd8WfTyjJSVggoAMMux1VOGFIS4C6tfRUeGFs-AVUNs8nr_t8a19EGu9PnhcyIXP3Xr0ZzO5ksdsd5k4UagHMjZ5CR8oh8ZHr1apUGqgxHWKS5vPCZiJdfrW-jkWxcvL3dEWw48zi58kQsd6_iyTAmRwuYQasBazG2qpZu1RCZwuO_1p8pfCKhRHKrdbiH8s5Jm-WGv0qrlx6Dkp2FOBa_o9DF6UhWCnBJhBi6uKWPgeASYfhGrFto7dCzErnZrLNLEsGGBprA"  # Replace with your actual access token

BASE_URL = "https://api.linkedin.com/v2/"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0"
}

response = requests.get(f"{BASE_URL}me", headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    urn = data.get('id')  # URN of the authenticated user
    print(f"Your LinkedIn URN is: {urn}")
else:
    print(f"Failed to fetch URN. Status Code: {response.status_code}")