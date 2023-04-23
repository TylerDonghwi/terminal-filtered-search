import webbrowser
import sys
import json
from os.path import dirname, abspath


def get_filter():
  filter_path =dirname(abspath(__file__))
  
  with open(str(filter_path) + '\\filter_website.json') as f:
    data = json.load(f)
    
  return data['filter']

def add_filter():
  filter = get_filter()
  res = ' ('
  for f in filter:
    res += 'site:' + f
    if (f != filter[-1]):
      res += ' OR '
    
  return res + ')'

def search():
  if (len(sys.argv) == 1):
    print("enter something to search for")
  else:
    url = 'https://www.google.com/search?q=' + '+'.join(sys.argv[1:]) + add_filter()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
search()
