#scraper.py
#from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
import urllib.request

def build_dir(dirName):
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:
        print("Directory " , dirName ,  " already exists")

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

class Scrape:
    def __init__(self, source):
        opener = AppURLopener()
        page_html = opener.open(source).read()
        # req = Request(source)
        # page_html = urlopen(req).read()
        self.soup = BeautifulSoup(page_html, "html.parser")

    def get(self, tag):
        return self.soup.select_one(tag)

    def get_all(self, tag):
        # tag_class = tag.split(', ')
        # print(tag_class)
        return self.soup.select(tag)
