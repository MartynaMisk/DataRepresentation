from bs4 import BeautifulSoup

with open("../Lab01-HTML.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

#print(soup.tr)

rows = soup.findAll("tr")
for row in rows:
    print("-----")
    #print(row)
    dataList = []
    cols = row.findAll("td")
    for col in cols:
        dataList.append(col.text)
    print(dataList)