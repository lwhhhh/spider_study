# coding:utf8
from imp import reload

from baike_spider import url_manager
from baike_spider import html_downloader,html_parser,html_output

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    #爬虫的调度方法
    def craw(self,root_rul):
        count = 1
        self.urls.add_new_url(root_rul)
        for i in self.urls.new_urls:
            print(i)
        while self.urls.has_new_url():
            try:
                print("@")
                new_url = self.urls.get_new_url()
                print("**",new_url)
                print(count)
                html_cont = self.downloader.download(new_url)
                print("html_cont=",html_cont)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                print("new_urls,new_data",new_url,new_data)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except:
                print("craw failed")


        self.output.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw("http://baike.baidu.com/view/21087.htm")

