import requests

from operator import itemgetter

# Make an API call and store the response

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)

print("Status Code:", r.status_code)
