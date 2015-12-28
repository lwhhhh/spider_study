# coding : "utf-8"
import urllib.request
import http.cookiejar

#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
    "Cookie":"_T_WM=cc6ac54e76a08597e9a47a9b8296b40d; SUHB=0N2kMPb2B_89ns; SUB=_2A257hV2jDeTxGedJ7VsX9yfJzjmIHXVYhmPrrDV6PUJbrdANLUPnkW15b9i1ym3l7FuyA3O0w0eh_O7o7g..; gsid_CTandWM=4ut061ad1FtlB5XxTM8S47qnd8X"
}

url = "http://weibo.cn/album/albummblog/?rl=11&fuid=3217179555&page=2&vt=4"
request = urllib.request.Request(url,headers = headers)
#request = urllib.request.Request(url,headers = headers)
#cj = http.cookiejar.FileCookieJar("cookies.txt")
#opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = urllib.request.urlopen(request)
_cont = r.read().decode()
print(_cont)
fout = open("out.html","w",encoding = "utf-8")
fout.write("%s"%_cont)
fout.close()
#http://ww3.sinaimg.cn/large/bfc243a3gw1ezf8z3yy8qj20xc1e0kjm.jpg
#http://ww3.sinaimg.cn/wap240/bfc243a3gw1ezf8z3yy8qj20xc1e0kjm.jpg
#http://ww3.sinaimg.cn/large/bfc243a3gw1ezf8z3yy8qj20xc1e0kjm.jpg
