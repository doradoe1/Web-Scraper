### This scrip will connect to a website and scrape data from a table in the website. 
### The website we are using collects data from a table and will parse it into an exel
### file in the directory where the scrip is stored.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.skysports.com/premier-league-table/2019"
### Importing the needed libraries to build the script and establish the url from where the 
### script will be scraping information. 

response = requests.get(url)

#print(response.status_code)
### This was done as a test to ensure that we are getting a response from the url we are using. 

soup = BeautifulSoup(response.text, "html.parser")
EPLT_2020 = soup.find("table", class_ = "standing-table__table")

#print(EPLT_2020)
### This print was done as a test to ensure that we are getting the information from the website. 
### We got an output as HTML with the correct information. 

teams_list = []
### An empty list is created to store the values the for loops are going to create. 
### This will also enable us to use Pandas easier. 

for entries in EPLT_2020.find_all("tbody"):
     rows = entries.find_all("tr")
     for row in rows:
        dic = {}
        ### A dictionary is built to store values in key:value pairs. The key names will be defined in the code.
        dic["Team"] = row.find("td", class_ = "standing-table__cell standing-table__cell--name").text.strip()
        dic["Games Played"] = row.find_all("td", class_ = "standing-table__cell")[2].text
        dic["Games Won"] = row.find_all("td", class_ = "standing-table__cell")[3].text
        dic["Games Draw"] = row.find_all("td", class_ = "standing-table__cell")[4].text
        dic["Games Lost"] = row.find_all("td", class_ = "standing-table__cell")[5].text
        dic["Goals in Favor"] = row.find_all("td", class_ = "standing-table__cell")[6].text
        dic["Goals Against"] = row.find_all("td", class_ = "standing-table__cell")[7].text
        dic["Goal Difference"] = row.find_all("td", class_ = "standing-table__cell")[8].text
        dic["Points"] = row.find_all("td", class_ = "standing-table__cell")[9].text
        teams_list.append(dic)
        ### This is going to append the dictionary entries to the list we created earlier.
        ### In the second for loop, I had difficulties identifying the index of each td tag, so I went through 
        ### a trial and error process until I found the order I wanted. At the end, I simply decided to include 
        ### most of the td tags to build a better table. 

print(teams_list)
### This print was done to ensure we don't have any errors in the dictionary and that it appended correctly 
### to the list created prior to starting the loop. 

df = pd.DataFrame(teams_list)
df.to_excel("Premier_League_Table_2019-2020_Seasson_Second_Copy.xlsx", index = False)

