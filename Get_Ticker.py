# Gather all tickers from S&P 500 by scraping from website
import requests
import random
from bs4 import BeautifulSoup

url = "https://stockanalysis.com/list/sp-500-stocks/"
tickers = []
r = requests.get(url) # Download the page
soup = BeautifulSoup(r.text, "html.parser") # Parse the data
Sym_table = soup.find('table', class_ ="symbol-table svelte-eurwtr") # Find the table (class) for symbols

# Loop through table to find all symbols
for sym in Sym_table.find_all("tbody"):
    rows = sym.find_all("tr")
    for row in rows:
        symbol = row.find("td", class_ = "sym svelte-eurwtr").text
        tickers.append(symbol)

