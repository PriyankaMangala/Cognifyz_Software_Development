import requests
from bs4 import BeautifulSoup
url = input("Enter website URL: ")
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException:
    print("Unable to access the website.")
    exit()

print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title

if title:
    print("Page title:", title.text)
else:
    print("No title found.")

headings = soup.find_all(["h1", "h2", "h3"])

print("\nHeadings:")

if headings:
    for heading in headings:
        print(heading.text.strip())
else:
    print("No headings found.")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

print("\nQuotes:")

for quote, author in zip(quotes, authors):
    print("Quote:", quote.text)
    print("Author:", author.text)
    print("--------------------")