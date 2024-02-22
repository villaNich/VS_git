from bs4 import BeautifulSoup
import requests 
import pandas as pd

#url = 'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
tab = soup.find_all('table')[1]
##print(tab)
titles = tab.find_all('th')
#print(titles)

all_titles = [title.text.strip() for title in titles]
#print(all_titles)

df = pd.DataFrame(columns = all_titles)

column_data = tab.find_all('tr')
for row in column_data[1:]: 
    row_data= row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)

    length = len(df)
    #print(length)
    
    df.loc[length] = individual_row_data
df   
