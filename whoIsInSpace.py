import requests

response = requests.get('http://api.open-notify.org/astros.json') #Open Notify api for folx in space
json = response.json()

print('The people currently in space are:')
for person in json['people']:
    print(person['name'])
