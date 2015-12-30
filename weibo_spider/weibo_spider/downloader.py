import urllib.request
import urllib.response
import http.cookies
import http.cookiejar

class Downloader(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
            "Cookie":"_T_WM=cc6ac54e76a08597e9a47a9b8296b40d; SUHB=0z1R4UnpHGixH7; SUB=_2A257huqdDeTxGedJ7VsX9yfJzjmIHXVYiPbVrDV6PUJbrdAKLRWlkW1dHEPjo-mdZIwS0i6qFlvmu0EM5w..; gsid_CTandWM=4u1U61ad1gJgI3DrJwmXs7qnd8X"
        }

    def download_page_cont(self, url):
        if url is None:
            return
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        page_cont = response.read().decode("utf-8")

        return page_cont

    def download_img(self, url):
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        img = response.read()
        return img




