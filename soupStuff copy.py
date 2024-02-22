from bs4 import BeautifulSoup
import requests

url = "https://www.oddsshopper.com/tools/arbitrage/CO"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'css')
newSoup = soup.find('table',
                    class_='MuiGrid-root MuiGrid-grid-xs-12 css-7j6nx7')
print(newSoup)
