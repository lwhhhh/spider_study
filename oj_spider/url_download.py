import urllib.request
import urllib.response
import http.cookies
import http.cookiejar


class Downloader(object):

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
            "Cookie": "PHPSESSID=qqcl9ai55vqqcliahl36la2kp7"
        }

    def download_page(self, url):
        if url is None:
            return
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        page_cont = response.read().decode("utf-8")

        return page_cont

    #def get_problem_links(self):
