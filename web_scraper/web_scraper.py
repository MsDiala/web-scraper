 
import requests
from bs4 import BeautifulSoup
import re


def get_soup_from_site(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  # soup.prettify()
  return soup

def get_citations_needed_count(url):
  soup = get_soup_from_site(url)
  all_citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
  return len(all_citations_needed)
  
def get_citations_needed_report(url):
  soup = get_soup_from_site(url)
  all_citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

  string_of_passages = ""
  
  for citation_needed in all_citations_needed:
    p_tag = citation_needed.find_parent('p')
    string_of_passages += p_tag.text.strip()
    string_of_passages += "\n\n"

  return string_of_passages


  #notes
  # for passage_needing in all_passages_needing:
  #   # each new citation is a new BeautifulSoup object.
  #   # it has each of the same methods available as the original soup
  #   print(passage_needing.text, end="\n"*3)



if __name__ == "__main__":
  url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
  print("count of citations needed is: ",get_citations_needed_count(url))
