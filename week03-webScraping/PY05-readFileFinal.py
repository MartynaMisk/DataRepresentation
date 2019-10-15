from bs4 import BeautifulSoup

with open("../Lab01-HTML.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

#print(soup.tr)
employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")
for row in rows:
    
    dataList = []
    cols = row.findAll("td")
    for col in cols:
        dataList.append(col.text)
    employee_writer.employee_writer(dataList)
employee_file.close()