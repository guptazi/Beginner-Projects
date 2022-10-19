import requests
from bs4 import BeautifulSoup
url= 'https://codewithharry.com'

#step 1 get the html

r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
paras=soup.find_all('p')
anchors=soup.find_all('a')
print(soup.find('p')['class'])