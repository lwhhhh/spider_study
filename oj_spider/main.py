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

    def login(self, username, password):
        login_page = self.downloader.download_page(
            "http://172.21.85.56/oj/auth/login?redirect=")

        login_result = self.parser.login_parser(login_page)
        print(login_result)
        if login_result == "failure":
            return "failure"
        elif login_result == "success":
            return "success"

    def craw(self, root_url):
        page = self.downloader.download_page(
            "http://172.21.85.56/oj/auth/login?redirect=")

        link_1 = self.parser.get_userhome_link(page)

        page_1 = self.downloader.download_page(link_1)  # User's page

        username = self.parser.get_username(page_1)
        self.output.mk_root_dir(username)

        problem_links = self.parser.get_problem_links(page_1)  # User页面下所有问题的链接
        mark = 0

        for i in range(10):

            page = self.downloader.download_page(
                problem_links[i])  # 一道题的提交记录页面(第一页)
            print(problem_links[i])
            report_dict = {}
            next_page_url = self.parser.get_report(page, report_dict)
            #report_dict, = self.parser.get_report(page)
            for key in report_dict:
                page_code = self.downloader.download_page(
                    report_dict[key]["code_url"])
                code = self.parser.get_codes(page_code)
                self.output.html_output(code, report_dict[key], os.getcwd())

            # 若这道题的提交记录还有下一页
            while next_page_url != None:
                print(next_page_url)
                page = self.downloader.download_page(next_page_url)
                next_page_url = self.parser.get_report(page, report_dict)

                for key in report_dict:
                    page_code = self.downloader.download_page(
                        report_dict[key]["code_url"])
                    code = self.parser.get_codes(page_code)
                    self.output.html_output(
                        code, report_dict[key], os.getcwd())
            print("Download no.%d successfully." % mark)
            mark = mark + 1

if __name__ == "__main__":
    print("ZQU OJ 代码下载器 \nversion 0.9")
    name = input("OJ username:")
    password = input("OJ password:")
    obj_spider = Spider(name, password)
    print("\n登录中...")
    while obj_spider.login(name, password) != "success":
        print("登录失败,有可能是用户名或者密码输错[没有账号跟钟鏸老师要]")
        name = input("OJ username:")
        password = input("OJ password:")
    print("登录成功...")
    print("程序运行完毕后会自动退出,你的代码放在该程序目录下")
    print("代码下载中...请等待")
    obj_spider.craw(root_url)
