import requests
from bs4 import BeautifulSoup

#fetching the data
response = requests.get("https://www.billboard.com/charts/hot-100/")
data = response.text

#parsing html
soup = BeautifulSoup(data,'html.parser')
rows = soup.find_all('div', {"class" : "o-chart-results-list-row-container"})
rawDict = {}
for row in rows:
    rawDict[(row.select('li')[4].find('h3').text).strip()] = row.select('li')[4].find('span').text.strip()

#sorting based on length of track
sortedDict={}
k = list(rawDict.items())
k.sort(key=lambda x:len(x[0]),reverse=False)
for i in k :
    sortedDict.update({i[0]:i[1]})

#printing list of artists as per sorting criteria
print(list(sortedDict.values()))


