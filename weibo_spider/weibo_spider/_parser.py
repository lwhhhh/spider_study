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
        self.links = soup.find_all()
        for link in self.links:
            print(link)

    def parse(self, page_cont):
        if page_cont is None:
            return

        self.get_all_links(page_cont)

        return self.links
