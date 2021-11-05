#!/usr/bin/env python3

# ---<=> MODULOS <=>---
import requests
from bs4 import BeautifulSoup

# ---<=> FUNCIONES <=>---
def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")
    
def wiki():
    soup = get_soup("https://en.wikipedia.org/wiki/List_of_states_of_Mexico")
    rows = soup.find_all("table")[0].find_all("tr")
    file = open('Scrapping.txt', "a")
    for row in rows:
        columns = row.find_all("td")
        t = [ele.text.strip() for ele in columns]
        file.write(f"{t}\n")
    file.close()

if __name__ == "__main__":
    wiki()
