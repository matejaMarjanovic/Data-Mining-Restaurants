import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

salariesUrl = "http://www.nationmaster.com/country-info/stats/Cost-of-living/Average-monthly-disposable-salary/After-tax"

uClient = uReq(salariesUrl)
pageHtml = uClient.read()
uClient.close()

pageSoup = soup(pageHtml, "html.parser")
allRows = pageSoup.table.findAll("tr")[1:]

df = pd.DataFrame(columns = ["Country", "Average Salary"])

for row in allRows:
    country = row.a.span.text
    avgSalary = float(row.findAll("td", {"class":"amount"})[0].text.strip()[1:].replace(",", ""))
    df = df.append({"Country" : country, "Average Salary" : avgSalary*0.857255035}, ignore_index = True)
    
with open("countrySalaries.csv", "w") as csvFile:
    csv = df.to_csv(index = True)
    csvFile.write(csv)
