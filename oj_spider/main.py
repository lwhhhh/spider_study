"""
爬取在学校oj提交过的代码
"""
import output
import url_manager
import url_download
import url_parser
import time
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
        # print(login_result)
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
        mark = 1

        # 一个提交页面一个dict,所有dict存放在一个list中.一道题可以有多个dict,但只能有一个list
        for i in range(200):
            report_list = []
            page = self.downloader.download_page(
                problem_links[i])  # 一道题的提交记录页面(第一页)
            # print(problem_links[i])
            report_dict = {}
            report_dict, next_page_url = self.parser.get_report(page)
            report_list.append(report_dict)
            # ↑ 第一页信息有了
            # for l in report_list:
                # for key in l:
                    # rint(key)
            # 处理多页提交
            while next_page_url != None:
                # print(next_page_url)
                report_dict_t = {}
                next_page = self.downloader.download_page(next_page_url)
                report_dict_t, next_page_url = self.parser.get_report(
                    next_page)
                #print(report_dict_t, next_page_url)
                report_list.append(report_dict_t)

            # 获取代码
            # print(report_list[0])
            for l in report_list:
                for key1 in l:
                    code_page = self.downloader.download_page(
                        l[key1]["code_url"])
                    code_source = self.parser.get_codes(code_page)
                    l[key1]["code"] = code_source
                    print(key1, "->", l[key1])

            # 输出代码到文件
            print("finish %d\n" % mark)
            mark = mark + 1


class LoginError(Exception):
    pass

if __name__ == "__main__":
    print("ZQU OJ 代码下载器 \nversion 0.9")
    name = input("OJ username:")
    password = input("OJ password:")
    obj_spider = Spider(name, password)
    print("\n登录中...")
    login_res = obj_spider.login(name, password)
    if(login_res != "success"):
        print("登录失败,有可能是用户名或者密码输错[没有账号跟钟鏸老师要]\n")
        print("程序初始化失败,5s后退出")
        time.sleep(5)
    else:
        print("登录成功...")
        print("程序运行完毕后会自动退出,你的代码放在该程序目录下")
        print("代码下载中...请等待")
        obj_spider.craw(root_url)
    a = input()
