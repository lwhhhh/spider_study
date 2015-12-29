import urllib.request
import urllib.response
import http.cookies
import http.cookiejar

class Downloader(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
            "Cookie":"_T_WM=cc6ac54e76a08597e9a47a9b8296b40d; SUHB=0N2kMPb2B_89ns; SUB=_2A257hV2jDeTxGedJ7VsX9yfJzjmIHXVYhmPrrDV6PUJbrdANLUPnkW15b9i1ym3l7FuyA3O0w0eh_O7o7g..; gsid_CTandWM=4ut061ad1FtlB5XxTM8S47qnd8X"
        }

    def download_page_cont(self, url):
        if url is None:
            return
        request = urllib.request.Request(url,headers = self.headers)
        response = urllib.request.urlopen(request)
        page_cont = response.read().decode("utf-8")

        return page_cont

    def download_img(self, url):
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        img = response.read()
        return img




