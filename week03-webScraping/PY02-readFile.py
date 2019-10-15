from bs4 import BeautifulSoup

with open("../Lab01-HTML.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print(soup.prettify())