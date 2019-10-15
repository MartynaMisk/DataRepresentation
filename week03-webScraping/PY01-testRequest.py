import requests
page = requests.get("https://www.myhome.ie")
print (page)
print("-------------------")
print (page.content)