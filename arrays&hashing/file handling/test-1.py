import requests
def fetch():
    r = requests.get('https://api.restful-api.dev/objects?id=3&id=5&id=10')
    print(r)

fetch()