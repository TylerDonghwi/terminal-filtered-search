import webbrowser
import sys


# filter = ['site:youtube.com']

url = 'https://www.google.com/search?q=' + '+'.join(sys.argv[1:])

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)