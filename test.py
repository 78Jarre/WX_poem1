import requests

with requests.get('http://127.0.0.1:5000/poem') as response:
    print(response.json())