"""
API Consumption (Requests Library)

    Use the requests library to fetch data from a public API 
    (e.g., JSONPlaceholder: https://jsonplaceholder.typicode.com/posts).
    Print the titles of all posts.
    Handle potential errors (e.g., no internet, API not responding).
"""
import requests

try:
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
except requests.ConnectTimeout as ex:
    print(f"==ERROR==\n\t{ex}")
except requests.ConnectionError as ex:
    print(f"==ERROR==\n\t{ex}")
except requests.HTTPError as ex:
    print(f"==ERROR==\n\t{ex}")
except requests.JSONDecodeError as ex:
    print(f"==ERROR==\n\t{ex}")
except requests.ReadTimeout as ex:
    print(f"==ERROR==\n\t{ex}")
except requests.Timeout as ex:
    print(f"==ERROR==\n\t{ex}")
except Exception as ex:
    print(f"==ERROR==\n\t{ex}")
else:
    datos = r.json()
    # Print the titles of all posts
    for post in datos:
        print(post["title"])

