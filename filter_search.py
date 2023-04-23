import webbrowser
import sys


filter = ['reddit.com', 'stackoverflow.com', 'stackexchange.com', 'youtube.com', 'github.com', ]

def add_filter():
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
