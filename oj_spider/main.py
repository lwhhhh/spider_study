"""
爬取在学校oj提交过的代码
"""
import output
import url_manager
import url_download
import url_parser
import os

root_url = "http://172.21.85.56/oj/"


class Spider(object):

    def __init__(self):
        self.manager = url_manager.Manager()
        self.downloader = url_download.Downloader()
        self.parser = url_parser.Parser()
        self.output = output.Output()

    def craw(self, root_url):
        page = self.downloader.download_page("http://172.21.85.56/oj/")
        # print(page)
        link_1 = self.parser.get_userhome_link(page)
        print(link_1)

        page_1 = self.downloader.download_page(link_1)
        # self.output.html_output(page_1)

        problem_links = self.parser.get_problem_links(page_1)
        # print(problem_links)

        page = self.downloader.download_page(problem_links[0])

        # 获取报告dict
        report_dict = self.parser.get_report(page)
        for key in report_dict:
            page_code = self.downloader.download_page(
                report_dict[key]["code_url"])
            code = self.parser.get_codes(page_code)
            self.output.html_output(code, report_dict[key],os.getcwd())
"""
        # 获取代码页面链接
        code_info_dict = self.parser.get_code_links(page)

        # 获取代码内容
        page_code = self.downloader.download_page(
            "http://172.21.85.56/oj/exercise/sourcecode?status_id=343478")
        # print(page_code)
        # self.output.html_output(page_code)
        code = self.parser.get_codes(page_code)
        # print(code)
"""

if __name__ == "__main__":
    obj_spider = Spider()
    obj_spider.craw(root_url)
