"""
爬取在学校oj提交过的代码
"""
import output
import url_manager
import url_download
import url_parser
import time
import os
import analysis

root_url = "http://172.21.85.56/oj/"
base_dir = os.getcwd()


class Spider(object):

    def __init__(self, name, password):
        self.manager = url_manager.Manager()
        self.downloader = url_download.Downloader(name, password)
        self.parser = url_parser.Parser()
        self.output = output.Output()
        self.analyser = analysis.Analyse()
        self.t_dict = {}
        self.codeline_count = 0
        self.name_true = ""

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

        self.name_true = self.parser.get_username(page_1)
        user_dir = self.output.mk_root_dir(self.name_true)
        print("文件夹创建成功")

        problem_links = self.parser.get_problem_links(page_1)  # User页面下所有问题的链接
        mark = 1

        # 一个提交页面一个dict,所有dict存放在一个list中.一道题可以有多个dict,但只能有一个list
        for i in range(0):
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
                # print(report_dict_t, next_page_url)
                report_list.append(report_dict_t)

            # 获取题号
            problem_id = ""
            problem_status = ""
            for d in report_list[0]:
                problem_id = report_list[0][d]["Pro.ID"]
                problem_id = problem_id.strip("\n")
                problem_status = report_list[0][d]["Status"]
                problem_status = problem_status.strip("\n")
                break
            self.t_dict[problem_id] = report_list
            problem_url = (
                "http://172.21.85.56/oj/exercise/problem?problem_id=" + problem_id)

            # 获取题目名称,输出的时候做文件名用
            problem_page = self.downloader.download_page(problem_url)
            title = self.parser.get_title(problem_page)
            title = title.strip("\n")
            title = title.replace(":", "-")
            title = title.replace("、", ",")
            title = title.replace("/", " ")
            title = title.replace("\\", " ")
            title = title.replace("?", ".")
            title = title.replace("*", ".")
            dir_name = problem_id + " " + title

            file_dir = self.output.mk_problem_dir(user_dir, dir_name)
            # print(file_dir)
            # 获取代码
            for l in report_list:
                for key in l:
                    code_page = self.downloader.download_page(
                        l[key]["code_url"])
                    code_source = self.parser.get_codes(code_page)
                    l[key]["code"] = code_source
                    content_io = l[key]["code"]
                    file_name = (
                        l[key]["Status"] + " " + l[key]["Submit Time"]).replace(":", "-") + ".cpp"
                    file_name = file_name.strip("\n")
                    content_io = code_source
                    self.output.html_output(content_io, file_dir, file_name)
                    # print(file_name)

           # print(dir_name)

            # file_name =
            io_content = ""
            # 输出代码到文件
            problem_url = report_list[0]
            print("finish %d\n" % mark)
            mark = mark + 1
            # self.t_list.append(report_list)

    def isnote(self, line):
        line = line.strip()
        # print(line, line_count)
        if len(line) >= 2:
            # print("***")
            # print("&&&", line[0], line[1])
            if line[0] == 47 and line[1] == 47:
                return "//"
            elif line[0] == 47 and line[1] == 42:
                return "/*"
            else:
                return "no"
        return "no"

    def analyse(self, code_count, note_count):
        # 先分析代码行数
        root_dir = base_dir + "/" + self.name_true
        for parent, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                os.chdir(parent)
                print(filename)
                print(parent)
                with open(filename, "rb") as f:
                    line = f.readline().strip()
                    print(line)
                    while line != b"":
                        # print("*")
                        #code_count = code_count + 1
                        ret = self.isnote(line)
                        print("ret=%s" % ret)
                        if ret == "//":
                            note_count = note_count + 1
                        elif ret == "/*":
                            line = f.readline().strip()
                            # print(line)
                            # if len(line) >= 2:
                            while b"*/" not in line:
                                line = f.readline().strip()
                                note_count = note_count + 1
                                print(line)
                        else:
                            code_count = code_count + 1
                        line = f.readline().strip()
                        print(line)

        return code_count, note_count


class LoginError(Exception):
    pass

if __name__ == "__main__":
    print("OJ 代码下载器 \nversion 0.9")
    name = input("OJ username:")
    password = input("OJ password:")
    obj_spider = Spider(name, password)
    print("\n登录中...")
    login_res = obj_spider.login(name, password)
    if(login_res != "success"):
        print("登录失败,有可能是用户名或者密码输错[没有账号跟钟鏸老师要]\n")
        print("程序初始化失败,3s后退出")
        time.sleep(3)
    else:
        print("登录成功...")
        print("程序运行完毕后会自动退出,你的代码放在该程序目录下")
        print("代码下载中...请等待")
        time_start = time.clock()
        obj_spider.craw(root_url)
        time_end = time.clock()
        print("下载完毕,用时%d s" % (time_end - time_start))
        print("开始分析你的代码...")
        code_count = 0
        note_count = 0
        code_count, node_count = obj_spider.analyse(code_count, note_count)
        print("代码行数: %d" % code_count)
        print("注释行数: %d" % node_count)
        # a = input()
