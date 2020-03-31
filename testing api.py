import requests
username = "danimc55"
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
for i in range(0,len(json)):
  print(json[i]['name'])
  print(json[i]['description'])
  

  