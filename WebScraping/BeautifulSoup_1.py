from bs4 import BeautifulSoup
import requests

url = "http://www.state.gov/secretary/travel/index.htm"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")

x = soup.find(id="total-mileage")
print(x.main.article.text)