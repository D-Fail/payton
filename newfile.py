

# Replace with the client ID and redirect URI of your test application
CLIENT_ID = 'your_client_id'
REDIRECT_URI = 'http://your-redirect-uri.com/callback'

# OAuth 2.0 authorization request
auth_url = f'https://www.facebook.com/v10.0/dialog/oauth?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=email'

# Redirect the user to the authorization URL
print(f"Go to the following URL to authorize the application:\n{auth_url}")

# Capture the authorization code from the redirect URI
code = input("Enter the authorization code from the redirect URI: ")

# Exchange the authorization code for an access token
token_url = 'https://graph.facebook.com/v10.0/oauth/access_token'
token_data = {
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'client_secret': 'your_client_secret',
    'code': code
}

response = requests.get(token_url, params=token_data)
access_token = response.json().get('access_token')

# Use the access token to make API requests
if access_token:
    print(f"Access Token: {access_token}")
    # Example API request
    user_info_url = f'https://graph.facebook.com/me?access_token={access_token}'
    user_info = requests.get(user_info_url).json()
    print(f"User Info: {user_info}")
else:
    print("Failed to obtain access token.")
    
