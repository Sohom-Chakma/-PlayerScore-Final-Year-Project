import streamlit as st

# setting page configurations
st.set_page_config(
    page_title="Data Cleaning",
    page_icon=":soccer:"
)

#creating sidebar with caption
st.sidebar.success("Explore my project!")

st.title("Extracting and Cleaning")


# Section 1: Initializing BeautifulSoup with code
st.subheader("Initializing URL using BeautifulSoup")
st.write("I use BeautifulSoup to parse the HTML code so that I can specify from where to get the links so I can use Pandas' 'read_html' method to get the structured data.")
st.code("""
from bs4 import BeautifulSoup
import requests

# Pulling desired links using BeautifulSoup
data = requests.get(url)
soup = BeautifulSoup(data.text)

# Identifying css elements containg desired links
cat_section = soup.select("div.section_content")
links = [l.get("href") for l in cat_section[0].find_all('a')]
        
# extracting desired links for outfield players and putting it into a list
links = [l for l in links if '/players/' in l and '/keepers' not in l and '/stats/' not in l and '/playingtime/' not in l and  '/passing_types/' not in l]
cat_urls = [f"https://fbref.com{l}" for l in links]

# getting link for previous season
soup.select("a.prev")[0].get("href")
""")

#Section 2: Web Scraper Loop Function
st.subheader("Creating Web Scraper")
st.write("First I will get the data for outfield players only. This loop reads HTML tables, gets rid of the multi-level columns but combining the names, merges all objects in the tables and seasonal lists and finally merges them all vertically by concatinating them.")
st.code("""
import pandas as pd
import time
from functools import reduce

# tables will contain stats for each category in a season
tables = []

# will contains merged tables for each season
seasonal = []

for year in years:

  # Pulling desired links using BeautifulSoup

  data = requests.get(url)
  soup = BeautifulSoup(data.text)

  cat_section = soup.select("div.section_content")
  links = [l.get("href") for l in cat_section[0].find_all('a')]
  links = [l for l in links if '/players/' in l and '/keepers' not in l and '/stats/' not in l and '/playingtime/' not in l and  '/passing_types/' not in l]
  cat_urls = [f"https://fbref.com{l}" for l in links]

  for i in cat_urls:
    stat = pd.read_html(i)[0]
    tables.append(stat)
    time.sleep(1)

  for t in tables:
    # creating a data with the same headers but without multi indexing
    t.columns = [' '.join(col).strip() for col in t.columns]
    t = t.reset_index(drop=True)

  for t in tables:
    # creating a list with new names
    new_columns = []
    for col in t.columns:
      if 'level_0' in col:
        new_col = col.split()[-1]  # takes the last name
      else:
        new_col = col
      new_columns.append(new_col)

    # rename columns
    t.columns = new_columns

  for i in tables:
    i['Age'] = i['Age'].str[:2]
    i['Nation'] = i['Nation'].str.split(' ').str.get(1)
    i['Comp'] = i['Comp'].str.split(' ').str[1:].str.join(' ')
    i.drop(['Rk', 'Matches', 'Age', 'Born'], axis = 1, inplace = True)
    i.drop_duplicates(keep=False, inplace = True)
    i = i.fillna(0, inplace=True)

  # merging all dataframes in table and appending it into a new table, seasonal.
  seasonal.append(reduce(lambda left, right:
              pd.merge(left, right, on = ['90s', 'Pos', 'Squad', 'Player', 'Nation', 'Comp']),
              tables))
  #resetting for next batch of tables
  tables = []

  #getting url for previous season
  previous_season = soup.select("a.prev")[0].get("href")
  url = f"https://fbref.com{previous_season}"
""")

# Section 3: Inserting a 'Season' column
st.write("Finally, I added a season column to help identify which season each entry belongs to.")
st.code("""
x = list(range(0,7,+1))

for i in x:
  try:
    seasonal[i]['Season']=years[i]
  except ValueError:
    continue
    
    df = pd.concat(seasonal)""")

# Section 4: Scraping and organizing GK data

st.write("The same loop was used for Goalkeepers with a minor change in the URL initialization with BeautifulSoup so that it targetted GK specific metrics.")

st.code("""
# targeting GK specific websites 
links = [l for l in links if '/players/' in l and '/keepers' in l]
""")