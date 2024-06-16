import requests
from bs4 import BeautifulSoup

def scrape_example(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").text
    return {"title": title}
