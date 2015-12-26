# coding:utf8

import urllib.request
import urllib.response
class HtmlDownloader(object):

    def download(self, url):
        print("in dow:",url)
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        cont = response.read()
        #print("!!",cont)
        if response.getcode() != 200:
            return None

        return cont
