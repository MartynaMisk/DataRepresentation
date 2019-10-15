import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

home_file = open('week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.find("div", class_="PropertyListingCard")
#print(listings)

for lisitng in listings:
    entryList = []

    price = listings.find(class_="PropertyListingCard__Price").text
    #print(price)
    entryList.append(price)
    address = listings.find(class_="PropertyListingCard__Address").text
    #print(adress)
    entryList.append(address)

    home_writer.writerow(entryList)
home_file.close()

