#!/usr/bin/env python3
#
# Auxiliary script for obtaining all inaugural speeches of all U.S.
# presidents from Wikipedia.

import re
import requests

from bs4          import BeautifulSoup
from urllib.parse import urljoin

def getName(title):
  i = title.index("'")
  n = title[:i]
  n = n.replace(" ", "_")

  return n

def getSpeech(name, url):
  page    = requests.get(url)
  content = page.content
  soup    = BeautifulSoup(content, "html.parser")
  header  = soup.find("div", class_="gen_header_title")
  div     = soup.find(id="mw-content-text")
  year    = re.search(r'\((\d+)\)', header.text).group(1)

  # Remove all licence containers
  licences = soup.find_all("div", class_="licenseContainer licenseBanner")
  for licence in licences:
    licence.decompose()
  
  speech = ""
  for p in div.find_all("p", recursive=True):
    speech += p.text + "\n"

  return year,speech
  

overviewURL     = "https://en.wikisource.org/wiki/Category:U.S._Presidential_Inaugural_Addresses"
baseURL         = urljoin(overviewURL, '/')
overviewPage    = requests.get(overviewURL)
overviewContent = overviewPage.content

soup = BeautifulSoup(overviewContent, "html.parser")

for category in soup.find_all("div", class_="mw-category-group"):
  ul = category.find("ul")
  for li in ul.find_all("li"):
    a    = li.find("a")
    page   = a['href']
    name   = getName(a.text)

    print("Processing %s..." % name)

    url          = urljoin(baseURL, page)
    year, speech = getSpeech(name, url)

    with open("%s.txt" % (year + "_" + name), "w") as f:
      f.write(speech)
