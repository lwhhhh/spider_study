import urllib.request
import urllib.response
import urllib.parse
import http.cookies
import http.cookiejar


class Downloader(object):

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
            #"Cookie": "PHPSESSID=qqcl9ai55vqqcliahl36la2kp7"
        }
        self.cookie_jar = http.cookiejar.CookieJar()
        cookie_ = urllib.request.HTTPCookieProcessor(self.cookie_jar)
        self.opener = urllib.request.build_opener(cookie_)
        self.post_dict = {
            "username": "201424133254",
            "password": "wh6625622",
            "submit:": "sign in"
        }
        #self.opener.addheaders = self.headers
        self.post_data = urllib.parse.urlencode(self.post_dict).encode()

    def download_page(self, url):
        if url is None:
            return

        #request = urllib.request.Request(url, headers=self.headers)
        #response = urllib.request.urlopen(request)
        response = self.opener.open(url, self.post_data)
        page_cont = response.read().decode("utf-8")
        print(page_cont)
        return page_cont

    # def get_problem_links(self):
