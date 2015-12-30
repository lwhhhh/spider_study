# coding : "utf-8"
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import urllib.request
import re


class Parser(object):
    def __init__(self):
        self.links = []

    def get_all_links(self, page_cont):
        soup = BeautifulSoup(page_cont, "html.parser", from_encoding="utf-8")
        #print(soup.prettify())
        self.tags = soup.find_all("img", src=re.compile(r".jpg"))
        # print(type(self.tags))
        for tag in self.tags:
            #print(tag)
            # temp_tag = BeautifulSoup(tag)
            link = tag.get("src")
            link = link.replace("square", "large")
            #(link)
            self.links.append(link)


    def parse(self, page_cont):
        if page_cont is None:
            return

        self.get_all_links(page_cont)

        return self.links
