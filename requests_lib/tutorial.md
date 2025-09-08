# Python Requests Library Tutorial: From Basic to Advanced

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Basic GET Requests](#basic-get-requests)
- [Understanding Response Objects](#understanding-response-objects)
- [Query Parameters](#query-parameters)
- [Headers](#headers)
- [POST Requests](#post-requests)
- [Other HTTP Methods](#other-http-methods)
- [Working with JSON](#working-with-json)
- [Sessions & Cookies](#sessions--cookies)
- [Authentication](#authentication)
- [Error Handling](#error-handling)
- [Timeouts](#timeouts)
- [File Operations](#file-operations)
- [Advanced Features](#advanced-features)
- [Best Practices](#best-practices)

## Introduction

The `requests` library is one of Python's most popular packages for making HTTP requests. It abstracts the complexities of making HTTP requests behind a simple API, making it perfect for interacting with web services.

## Installation

```python
# Install requests using pip
pip install requests

# Import the library
import requests
```

## Basic GET Requests

GET is the most common HTTP method used to request data from a specified resource.

```python
# Simple GET request
import requests

response = requests.get('https://api.github.com')

# Print the response status code
print(f"Status code: {response.status_code}")

# Print the response content
print(response.text[:100])  # First 100 characters
```

## Understanding Response Objects

Every request returns a Response object containing all the information returned by the server.

```python
import requests

response = requests.get('https://api.github.com')

# Status code
print(f"Status code: {response.status_code}")

# Response headers
print(f"Headers: {response.headers}")

# Content type
print(f"Content type: {response.headers['content-type']}")

# Encoding
print(f"Encoding: {response.encoding}")

# Response content as text
print(f"Text content: {response.text[:50]}...")

# Response content as bytes
print(f"Binary content: {response.content[:20]}...")

# Check if request was successful
if response.ok:
    print("Request was successful")
else:
    print("Request failed")

# Raise an exception for bad status codes
response.raise_for_status()
```

## Query Parameters

Adding query string parameters to your requests is straightforward.

```python
import requests

# Method 1: Using params parameter
params = {
    'q': 'python requests',
    'sort': 'stars',
    'order': 'desc'
}
response = requests.get('https://api.github.com/search/repositories', params=params)
print(f"URL: {response.url}")

# Method 2: Including parameters directly in URL
response = requests.get('https://api.github.com/search/repositories?q=python&sort=stars')
print(f"URL: {response.url}")

# Parse JSON response
data = response.json()
print(f"Total repositories: {data.get('total_count')}")
```

## Headers

HTTP headers let the client and server pass additional information with an HTTP request or response.

```python
import requests

# Setting custom headers
headers = {
    'User-Agent': 'Python Requests Tutorial',
    'Accept': 'application/json'
}

response = requests.get('https://api.github.com', headers=headers)
print(f"Request headers: {response.request.headers}")
print(f"Response headers: {response.headers}")

# Getting specific header values
print(f"Server: {response.headers.get('server')}")
print(f"Content-Type: {response.headers.get('content-type')}")
```

## POST Requests

POST requests are used to send data to a server to create or update a resource.

```python
import requests

# Simple POST request with form data
data = {
    'username': 'testuser',
    'password': 'password123'
}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())

# POST request with JSON data
json_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'message': 'Hello, world!'
}
response = requests.post('https://httpbin.org/post', json=json_data)
print(response.json())
```

## Other HTTP Methods

Requests supports all HTTP methods: GET, POST, PUT, DELETE, HEAD, OPTIONS.

```python
import requests

# PUT request
data = {'name': 'Updated Name'}
put_response = requests.put('https://httpbin.org/put', json=data)
print(f"PUT response: {put_response.status_code}")

# DELETE request
delete_response = requests.delete('https://httpbin.org/delete')
print(f"DELETE response: {delete_response.status_code}")

# HEAD request - get headers only, no body
head_response = requests.head('https://httpbin.org/get')
print(f"HEAD response: {head_response.headers}")

# OPTIONS request - get allowed methods
options_response = requests.options('https://httpbin.org/get')
print(f"OPTIONS response: {options_response.headers.get('Allow')}")
```

## Working with JSON

Many APIs return data in JSON format, and requests makes it easy to work with this data.

```python
import requests

response = requests.get('https://api.github.com/users/python')

# Parse JSON response
user_data = response.json()

# Access data
print(f"Username: {user_data['login']}")
print(f"Name: {user_data.get('name', 'N/A')}")
print(f"Followers: {user_data.get('followers', 0)}")

# Handling nested JSON
response = requests.get('https://api.github.com/repos/psf/requests')
repo_data = response.json()
print(f"Owner: {repo_data['owner']['login']}")
print(f"License: {repo_data.get('license', {}).get('name', 'N/A')}")
```

## Sessions & Cookies

Sessions allow you to persist parameters across requests and reuse connections.

```python
import requests

# Using a session
session = requests.Session()

# Session will maintain cookies
session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
response = session.get('https://httpbin.org/cookies')
print(f"Session cookies: {response.json()}")

# Manually setting cookies
cookies = {'manual_cookie': 'test_value'}
response = requests.get('https://httpbin.org/cookies', cookies=cookies)
print(f"Manual cookies: {response.json()}")

# Working with the cookies jar
session = requests.Session()
session.cookies.set('example_cookie', 'cookie_value', domain='httpbin.org')
response = session.get('https://httpbin.org/cookies')
print(f"Cookie jar: {response.json()}")
```

## Authentication

Requests supports various authentication methods.

```python
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

# Basic authentication
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=HTTPBasicAuth('user', 'pass')
)
print(f"Basic Auth: {response.status_code}")

# Shorthand for basic authentication
response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(f"Basic Auth (shorthand): {response.status_code}")

# Digest authentication
response = requests.get(
    'https://httpbin.org/digest-auth/auth/user/pass',
    auth=HTTPDigestAuth('user', 'pass')
)
print(f"Digest Auth: {response.status_code}")

# Token authentication
headers = {'Authorization': 'Bearer your_token_here'}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(f"Token Auth: {response.json()}")

# OAuth example (simplified)
from requests_oauthlib import OAuth1
auth = OAuth1('consumer_key', 'consumer_secret', 'token', 'token_secret')
response = requests.get('https://httpbin.org/headers', auth=auth)
print(f"OAuth1: {response.json()}")
```

## Error Handling

Proper error handling is crucial when making HTTP requests.

```python
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

url = 'https://httpbin.org/status/404'

# Method 1: Using try-except with raise_for_status()
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()
    print(data)
except HTTPError as e:
    print(f"HTTP error occurred: {e}")
except ConnectionError as e:
    print(f"Connection error occurred: {e}")
except Timeout as e:
    print(f"Timeout error occurred: {e}")
except RequestException as e:
    print(f"Error during request: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Method 2: Checking status code directly
response = requests.get('https://httpbin.org/status/500')
if response.status_code == 200:
    print("Request was successful")
elif response.status_code == 404:
    print("Resource not found")
elif response.status_code == 500:
    print("Server error")
else:
    print(f"Other status code: {response.status_code}")
```

## Timeouts

Setting timeouts prevents your application from hanging indefinitely.

```python
import requests
from requests.exceptions import Timeout

# Setting timeout (in seconds)
try:
    # Timeout for connection and read combined
    response = requests.get('https://httpbin.org/delay/3', timeout=2)
    print("Request completed")
except Timeout:
    print("The request timed out")

# Setting different timeouts for connection and read operations
try:
    # (connect timeout, read timeout)
    response = requests.get('https://httpbin.org/delay/1', timeout=(3, 5))
    print("Request completed with specific timeouts")
except Timeout:
    print("The request timed out")

# Disabling timeout (not recommended)
response = requests.get('https://httpbin.org/get', timeout=None)
```

## File Operations

Requests can handle file uploads and downloads.

```python
import requests

# Downloading a file
url = 'https://httpbin.org/image/jpeg'
response = requests.get(url, stream=True)

# Method 1: Save with open()
with open('image.jpg', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive chunks
            f.write(chunk)

# Method 2: Using shutil
import shutil
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open('image2.jpg', 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)

# Uploading files
files = {'file': open('image.jpg', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)
print(response.json())

# Uploading files with custom filename, content type and headers
files = {
    'file': ('report.jpg', open('image.jpg', 'rb'), 'image/jpeg', {'Expires': '0'})
}
response = requests.post('https://httpbin.org/post', files=files)
print(response.json())
```

## Advanced Features

### Proxies

```python
import requests

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

response = requests.get('https://httpbin.org/get', proxies=proxies)
print(response.json())

# Using HTTP Basic Auth with proxies
proxies = {
    'http': 'http://user:pass@10.10.1.10:3128',
}

# With environment variables
# Set HTTP_PROXY and HTTPS_PROXY environment variables
import os
os.environ['HTTP_PROXY'] = 'http://10.10.1.10:3128'
os.environ['HTTPS_PROXY'] = 'http://10.10.1.10:1080'
```

### SSL Verification

```python
import requests

# Disable SSL verification (not recommended for production)
response = requests.get('https://expired.badssl.com/', verify=False)
print(response.status_code)

# Suppress only the InsecureRequestWarning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Custom CA bundle
response = requests.get('https://github.com', verify='/path/to/certfile')
```

### Retries

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure retry strategy
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET", "POST"]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

response = session.get("https://httpbin.org/status/500")
```

### Custom Transport Adapters

```python
import requests
from requests.adapters import HTTPAdapter

class CustomAdapter(HTTPAdapter):
    def __init__(self, pool_connections=10, pool_maxsize=10, max_retries=0,
                 pool_block=False):
        super().__init__(pool_connections=pool_connections,
                         pool_maxsize=pool_maxsize, max_retries=max_retries,
                         pool_block=pool_block)
        
    def init_poolmanager(self, *args, **kwargs):
        kwargs['socket_options'] = [
            (socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
        ]
        super().init_poolmanager(*args, **kwargs)

session = requests.Session()
adapter = CustomAdapter()
session.mount('http://', adapter)
session.mount('https://', adapter)
```

### Streaming Large Responses

```python
import requests

# Stream response content
response = requests.get('https://api.github.com/events', stream=True)
for line in response.iter_lines():
    if line:  # filter out keep-alive new lines
        decoded_line = line.decode('utf-8')
        print(json.loads(decoded_line))

# Process response in chunks
response = requests.get('https://httpbin.org/stream/20', stream=True)
for chunk in response.iter_content(chunk_size=1024):
    if chunk:  # filter out keep-alive new chunks
        print(f"Got chunk of size {len(chunk)} bytes")
```

## Best Practices

### Connection Pooling

```python
import requests

# Session reuses the same TCP connection
session = requests.Session()

# Make multiple requests with the same session
for i in range(10):
    response = session.get(f'https://httpbin.org/get?id={i}')
    print(f"Request {i}: {response.status_code}")
```

### Setting User-Agent

```python
import requests

headers = {
    'User-Agent': 'MyApp/1.0 (your@email.com)'
}

response = requests.get('https://api.github.com', headers=headers)
print(response.json())
```

### Content Compression

```python
import requests

# Automatically handle gzip/deflate compression
headers = {'Accept-Encoding': 'gzip, deflate'}
response = requests.get('https://httpbin.org/gzip', headers=headers)
print(response.json())
```

### Hooks

```python
import requests

def print_url(response, *args, **kwargs):
    print(f"URL: {response.url}")
    print(f"Status Code: {response.status_code}")

hooks = {'response': print_url}
response = requests.get('https://httpbin.org/get', hooks=hooks)
```

### Connection Timeouts vs. Read Timeouts

```python
import requests

# Connection timeout: time to establish the connection to the server
# Read timeout: time to receive data after connection is established
response = requests.get('https://httpbin.org/delay/1', timeout=(3.05, 27))
```

### Rate Limiting

```python
import requests
import time

# Simple rate limiting
for i in range(5):
    response = requests.get('https://api.github.com/users/python')
    print(f"Request {i+1}: {response.status_code}")
    remaining = int(response.headers.get('X-RateLimit-Remaining', 0))
    print(f"Remaining requests: {remaining}")
    if remaining < 10:
        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
        sleep_time = reset_time - time.time()
        if sleep_time > 0:
            print(f"Rate limit almost reached. Sleeping for {sleep_time} seconds")
            time.sleep(sleep_time)
    # Be nice to the API
    time.sleep(1)
```

### Context Management

```python
import requests
import contextlib

# Using requests with context manager for auto-closing
with requests.Session() as session:
    response = session.get('https://httpbin.org/get')
    print(response.json())
    # session is automatically closed when exiting the with block

# Creating a custom context manager for API calls
@contextlib.contextmanager
def api_session(base_url, token=None):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'MyApp/1.0',
        'Accept': 'application/json',
    })
    
    if token:
        session.headers['Authorization'] = f'Bearer {token}'
        
    try:
        yield session
    finally:
        session.close()

# Using the custom context manager
with api_session('https://api.example.com', token='my_token') as session:
    response = session.get('/endpoint')
    print(response.json())
```

### Real-world Examples

#### Weather API Example

```python
import requests
import os

def get_weather(city):
    api_key = os.environ.get('WEATHER_API_KEY', 'your_api_key_here')
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error getting weather data: {e}")
        return None

# Example usage
get_weather('London')
```

#### GitHub API Example

```python
import requests
import json

def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    
    # If you have a GitHub token, you can authenticate to increase rate limits
    # headers['Authorization'] = f'token {your_token}'
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        repos = response.json()
        print(f"{username} has {len(repos)} public repositories:")
        
        for repo in repos:
            print(f"- {repo['name']}: {repo['description'] or 'No description'}")
            print(f"  Stars: {repo['stargazers_count']}, Forks: {repo['forks_count']}")
            print(f"  URL: {repo['html_url']}")
            print()
            
        return repos
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return None

# Example usage
get_github_repos('pallets')
```

#### Web Scraping Example

```python
import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

def scrape_python_news():
    url = "https://www.python.org/blogs/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.select('ul.list-recent-posts li')
        
        print("Latest Python News:")
        for item in news_items:
            title = item.find('a').text.strip()
            date = item.find('time').text.strip()
            link = "https://www.python.org" + item.find('a')['href']
            
            print(f"- {title} ({date})")
            print(f"  {link}")
            print()
            
    except requests.exceptions.RequestException as e:
        print(f"Error scraping Python news: {e}")

# Example usage
scrape_python_news()
```

#### Web API Authentication Example

```python
import requests
import json
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

# Basic Authentication
def basic_auth_example():
    url = "https://httpbin.org/basic-auth/user/pass"
    response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
    
    print("Basic Auth Status:", response.status_code)
    if response.status_code == 200:
        print("Authentication successful!")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Authentication failed")

# OAuth2 Authentication (simplified example)
def oauth2_example():
    # This is a simplified example, real OAuth2 implementation requires more steps
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    token_url = 'https://provider.com/oauth/token'
    
    # Typically, you'd need to go through the OAuth flow to get a token
    # This is just a simplified example of using a token you already have
    token = {
        'access_token': 'your_access_token',
        'token_type': 'Bearer',
        'expires_in': 3600
    }
    
    # Create an OAuth2 session
    oauth = OAuth2Session(client_id, token=token)
    response = oauth.get('https://api.example.com/resource')
    
    print("OAuth2 Example (simplified):")
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(response.text)

# API Key Authentication
def api_key_example():
    url = "https://api.example.com/data"
    params = {
        'api_key': 'your_api_key',
        'query': 'example'
    }
    
    # API key in query parameters
    response = requests.get(url, params=params)
    
    # Alternative: API key in header
    headers = {
        'X-API-Key': 'your_api_key'
    }
    response = requests.get(url, headers=headers)

# JWT Authentication
def jwt_example():
    # Assume you already have a JWT token
    jwt_token = "your.jwt.token"
    
    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }
    
    response = requests.get('https://api.example.com/protected', headers=headers)
    print(f"JWT Auth Status: {response.status_code}")
```

#### Downloading a Large File with Progress

```python
import requests
import os
from tqdm import tqdm  # pip install tqdm

def download_file(url, filename):
    """
    Download a file with progress bar
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        
        with open(filename, 'wb') as f:
            desc = f"Downloading {filename}"
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=desc) as pbar:
                for data in r.iter_content(block_size):
                    if data:  # filter out keep-alive new chunks
                        f.write(data)
                        pbar.update(len(data))

# Example usage
url = "https://speed.hetzner.de/100MB.bin"
download_file(url, "large_file.bin")
```

#### RESTful API Client Example

```python
import requests
import json

class APIClient:
    """A simple REST API client"""
    
    def __init__(self, base_url, token=None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'PythonAPIClient/1.0'
        })
        
        if token:
            self.session.headers['Authorization'] = f'Bearer {token}'
    
    def get(self, endpoint, params=None):
        """Make a GET request to the API"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint, data):
        """Make a POST request to the API"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint, data):
        """Make a PUT request to the API"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=data)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint):
        """Make a DELETE request to the API"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url)
        response.raise_for_status()
        return response.status_code
    
    def close(self):
        """Close the session"""
        self.session.close()

# Example usage
def main():
    # Create a client for JSONPlaceholder API
    api = APIClient('https://jsonplaceholder.typicode.com')
    
    try:
        # Get all posts
        posts = api.get('/posts')
        print(f"Found {len(posts)} posts")
        
        # Get a specific post
        post = api.get('/posts/1')
        print(f"Post 1 title: {post['title']}")
        
        # Create a new post
        new_post = {
            'title': 'My New Post',
            'body': 'This is the content of my new post',
            'userId': 1
        }
        created = api.post('/posts', new_post)
        print(f"Created post with ID: {created['id']}")
        
        # Update a post
        update_data = {
            'title': 'Updated Title',
            'body': 'Updated content',
            'userId': 1
        }
        updated = api.put('/posts/1', update_data)
        print(f"Updated post: {updated['title']}")
        
        # Delete a post
        status = api.delete('/posts/1')
        print(f"Delete status: {status}")
        
    finally:
        api.close()

if __name__ == "__main__":
    main()
```
