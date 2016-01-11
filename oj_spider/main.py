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

    def __init__(self, name, password):
        self.manager = url_manager.Manager()
        self.downloader = url_download.Downloader(name, password)
        self.parser = url_parser.Parser()
        self.output = output.Output()
        self.globe_dict = {}

    def craw(self, root_url):
        page = self.downloader.download_page(
            "http://172.21.85.56/oj/auth/login?redirect=")
        # print(page)
        # with open("ts.html", "w", encoding="utf-8") as f:
            # f.write(page)

        link_1 = self.parser.get_userhome_link(page)
        # print(link_1)

        page_1 = self.downloader.download_page(link_1)
        # with open("tss.html", "w", encoding="utf-8") as f:
            # f.write(page_1)
        username = self.parser.get_username(page_1)
        self.output.mk_root_dir(username)
       # print(username)
        problem_links = self.parser.get_problem_links(page_1)
        mark = 0
        # print(problem_links)
        for problem_link in problem_links:
            # print(problem_link)
            page = self.downloader.download_page(problem_link)
            # print(i)
            # 获取报告dict
            report_dict, next_page_url = self.parser.get_report(page)
            for key in report_dict:
                page_code = self.downloader.download_page(
                    report_dict[key]["code_url"])
                code = self.parser.get_codes(page_code)
                self.output.html_output(code, report_dict[key], os.getcwd())

            # 读取下一页
            while next_page_url != None:
                page = self.downloader.download_page(next_page_url)
                report_dict, next_page_url = self.parser.get_report(page)
                # if report_dict is None:
                    # return
                # print(report_dict)
                # if report_dict is None or next_page_url is None:
                    # return
                if len(report_dict) == 0:
                    break
                for key in report_dict:
                    page_code = self.downloader.download_page(
                        report_dict[key]["code_url"])
                    code = self.parser.get_codes(page_code)
                    self.output.html_output(
                        code, report_dict[key], os.getcwd())
            print("Download no.%d successfully." % mark)
            mark = mark + 1
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
    print("ZQU OJ 代码下载器 \nversion 0.9")
    name = input("oj username:")
    password = input("oj password:")
    print("请等待大概20s,运行过程中不要关闭窗口,程序运行完毕会自动退出 :)")
    print("输出文件存放在该程序相同的目录")
    obj_spider = Spider(name, password)
    obj_spider.craw(root_url)
