# coding:"utf-8"


class Manager(object):

    def geturls(self):
        url_const = "http://weibo.cn/album/albummblog/?rl=11&fuid=3217179555&page="
        urls = [url_const + str(x) for x in range(1, 55)]

        return urls
