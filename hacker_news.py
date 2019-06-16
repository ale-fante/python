import requests

from operator import itemgetter

# Make an API call and store the response

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)

print("Status Code:", r.status_code)

# Process information about each submission

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:10]:
	# Make a separate API call for each submission
	url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + '.json')

	submission_r = requests.get(url)
	#print(submission_r.status_code)
	response_dict = submission_r.json()
	#print(response_dict)

	submission_dict = {
		"title" : response_dict['title'],
		"link" : "http://news.ycombinator.com/item?id=" + str(submission_id),
		"comments" : response_dict.get("descendants", 0),
		"type" : response_dict['type'],
		"score" : response_dict['id'],
		"by" : response_dict['by'],
		"id" : response_dict['id']
	}

	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
	print("\nTitle:", submission_dict['title'])
	print("Author:", submission_dict['by'])
	print("Discussion link:", submission_dict['link'])
	print("Comments:", submission_dict['comments'])
	print("Type:", submission_dict['type'])
	print("ID:", submission_dict['id'])
