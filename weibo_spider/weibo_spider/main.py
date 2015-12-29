# coding : "utf-8"
# 爬取新浪微博账号"回忆专用小马甲"所发微博的所有图片
"""
思路: 图片来自54个网址,每个网址下来都有图片,爬下这些图片的地址,并更换图片地址中的参数,可以得到这些图片的原图

     main文件起调度作用,manager文件管理待爬的url,downloader文件负责从网址下载数据,parser文件解析数据,output负责保存数据
     url: http://weibo.cn/album/albummblog/?rl=11&fuid=3217179555&page=1,其中page的参数范围从1到54
"""

import manager,_parser,output,downloader

class Spider(object):
    def __init__(self):
        self.manager = manager.Manager()
        self.downloader = downloader.Downloader()
        self.parser = _parser.Parser()
        self.output = output.Output()

    def craw(self):
        urls = self.manager.geturls()
        for url in urls:
            print(url)
            page_cont = self.downloader.download_page_cont(url)
            img_links = self.parser.parse(page_cont)
            index = 1
            for img_link in img_links:
                print(img_link)
                img = self.downloader.download_img(img_link)
                self.output.output(img, index)
                index += 1


if __name__ == "__main__":
    obj_spider = Spider()
    obj_spider.craw()