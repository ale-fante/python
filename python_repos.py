# Must install:
# pip install --user requests

import requests

# Make an API call and store the response

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

print("Status code:" , r.status_code)

# Store API response in a variable

response_dict = r.json()

# Process results
print(response_dict.keys())

print("Total repositories:", response_dict['total_count'])

# More info about the repos
repo_dicts = response_dict['items']

print("Repositories returned", len(repo_dicts))

# Examine the first repo

repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))

for key in sorted(repo_dict.keys()):
	print(key)

print("Selected info about the first repo:")

print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('URL:', repo_dict['url'])