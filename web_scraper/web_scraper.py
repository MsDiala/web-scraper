import requests
from bs4 import BeautifulSoup 
import re

def get_citations_needed_count(url):

    response =requests.get(url)

    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    soup.find_all("a", href=True,title="Wikipedia:Citation needed")
    print(len(soup.find_all("a", href=True,title="Wikipedia:Citation needed")))


  
def get_citations_needed_report(url):
    response =requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    soup.find_all("p")
    print(len(soup.find_all("p")))






if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
 

