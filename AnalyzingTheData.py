python
import requests
url = 'https://api.github.com/user'
response = requests.get(url,auth=('userName','password'))
response.json()
my_json = response.json()
for key in my_json():
print(key)
my_json['id']

