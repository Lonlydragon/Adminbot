import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch")
soup = BeautifulSoup(response.content,"lxml")
price = soup.select('table td')
tesla = price[5].text

response2 = requests.get("https://finance.yahoo.com/quote/RUB=X?p=RUB=X&.tsrc=fin-srch")
soup2 = BeautifulSoup(response2.content,"lxml")
price2 = soup2.select('table td')
usdrub = price2[5].text

response3 = requests.get("https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch")
soup3 = BeautifulSoup(response3.content,"lxml")
price3 = soup3.select('table td')
apple = price3[5].text


print(tesla, usdrub, apple)