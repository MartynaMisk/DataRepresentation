import requests
import json 
#	creates	a	car	on	the	server	by	using	the	API
url = 'http://127.0.0.1:5000/cars'
dataString = {'reg':'08 C 1234','make':'Ford','model':'Galaxy','price':12324}

response = requests.post(url, json=dataString)
print (response.status_code)
print(response.json())