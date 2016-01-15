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
        self.total_submiss = 0
        self.total_ac = 0
        self.total_wa = 0
        self.total_tle = 0
        self.total_re = 0
        self.total_ce = 0
        self.total_wait = 0
        self.most_submiss = 0
        self.longest_run = ""
        self.max_memory = ""
        self.logest_code = ""

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
        for i in problem_links:
            report_list = []
            page = self.downloader.download_page(
                i)  # 一道题的提交记录页面(第一页)
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
            # print(self.t_dict[problem_id])
            # print("!!!!")
            # print(report_list)
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
                    #l[key]["code"] = code_source
                    content_io = code_source
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
            print("finish %d" % mark)
            mark = mark + 1
            break
            # self.t_list.append(report_list)

    def analyse(self, code_count):

        # 统计代码行数
        root_dir = base_dir + "/" + self.name_true
        for parent, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                os.chdir(parent)
                # print(filename)
                # print(parent)
                with open(filename, "rb") as f:
                    # 因为有CE代码的存在,可能导致判断注释代码的过程中陷入死循环,所以取消
                    line = f.readline().strip()
                    while line != b"":
                        if line != b"\n":
                            code_count = code_count + 1
                            line = f.readline().strip()

        # 生成时间,从2013-01至2016-12
        year_list = [y for y in range(2013, 2017)]
        month_list = []
        s = ""
        for m in range(1, 13):
            if m < 10:
                s = "0" + str(m)
            else:
                s = str(m)
            month_list.append(s)
            # print(s)
        date_list = [str(y) + "-" + str(m)
                     for y in year_list for m in month_list]
        date_dict = {}
        for d in date_list:
            date_dict[d] = 0
        # 好吧开始分析代码!!!
        """
            要分析的内容有:
            1.总提交数
            2.ac数
            3.wa数
            4.tle数
            5.re数
            6.ce数
            7.提过次数最多的题目
            8.运行时间最长的题目
            9.占用内存最多的题目
            10.代码最长的一次提交
        """
        # print(self.t_dict)
        problem_nums = 0
        sub_count_id = ""
        time_min = "999999999999"
        time_max = ""
        for problem_id in self.t_dict:
            problem_nums = problem_nums + 1
            sub_count = 0
            for li in self.t_dict[problem_id]:
                sub_count += len(li)
                if self.most_submiss < sub_count:
                    self.most_submiss = sub_count
                    sub_count_id = problem_id
                    # print(self.most_submiss,sub_count_id,"*")
                for key in li:
                    # print(key)
                    self.total_submiss = self.total_submiss + 1
                    status = li[key]["Status"]
                    if status == "AC":
                        self.total_ac = self.total_ac + 1
                    elif status == "WA":
                        self.total_wa = self.total_wa + 1
                    elif status == "RE":
                        self.total_re = self.total_re + 1
                    elif status == "CE":
                        self.total_ce = self.total_ce + 1
                    elif status == "TLE":
                        self.total_tle = self.total_tle + 1
                    elif status == "WAIT":
                        self.total_wait = self.total_wait + 1
                    time_temp = li[key]["Submit Time"]
                    time_temp_1 = time_temp[:7]
                    date_dict[time_temp_1] += 1
                    #print(time_temp_1)
                    if time_max < time_temp:
                        time_max = time_temp
                    if time_min > time_temp:
                        time_min = time_temp
        """
        self.most_submiss = ""
        self.longest_run = ""
        self.max_memory = ""
        self.logest_code = ""
        """
        report_res = []
        print("time", time_max, time_min)
        print("id=:", sub_count_id, "max: ", self.most_submiss)
        print("\nproblem_nums: %d " % problem_nums)
        print("Submission: %d " % self.total_submiss)

        report_res1 = {}
        # 总提交,ac数,wa数,tle数,re数,ce数,wait数,ac%,wa%,tle%,re%,ce%,wait%
        # 第一次在oj上的提交,最近一次提交
        report_res1["ts"] = str(self.total_submiss)
        report_res1["ac"] = str(self.total_ac)
        report_res1["wa"] = str(self.total_wa)
        report_res1["tle"] = str(self.total_tle)
        report_res1["re"] = str(self.total_re)
        report_res1["ce"] = str(self.total_ce)
        report_res1["wait"] = str(self.total_wait)
        report_res1["ac%"] = str(
            "%.2f" % (int(self.total_ac) / int(self.total_submiss) * 100))
        report_res1["wa%"] = str(
            "%.2f" % (int(self.total_wa) / int(self.total_submiss) * 100))
        report_res1["tle%"] = str(
            "%.2f" % (int(self.total_tle) / int(self.total_submiss) * 100))
        report_res1["re%"] = str(
            "%.2f" % (int(self.total_re) / int(self.total_submiss) * 100))
        print("AC: %d " % self.total_ac)
        self.total_ac = str(self.total_ac)
        report_res.append(self.total_ac)

        print("WA: %d " % self.total_wa)
        self.total_wa = str(self.total_wa)
        report_res.append(self.total_wa)

        print("RE: %d " % self.total_re)
        self.total_re = str(self.total_re)
        report_res.append(self.total_re)

        print("TLE: %d " % self.total_tle)
        self.total_tle = str(self.total_tle)
        report_res.append(self.total_tle)

        print("CE: %d " % self.total_ce)
        self.total_ce = str(self.total_ce)
        report_res.append(self.total_ce)

        print("WAIT: %d " % self.total_wait)
        self.total_wait = str(self.total_wait)
        report_res.append(self.total_wait)

        # print(base_dir)
        content = " "
        self.output.data_output(report_res, report_res1, base_dir, code_count)
        self.output.data_output2(date_list, date_dict, base_dir)
        return code_count


class LoginError(Exception):
    pass

if __name__ == "__main__":
    print("OJ 代码下载器 \nversion 0.98")
    print("/*\n author:14软件2班 lwh\n 联系方式:lwhile@outlook.com\n\n*/")
    name = input("OJ Username: ")
    password = input("OJ Password: ")
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
        code_count = obj_spider.analyse(code_count)
        print("分析完成.")
        print("代码行数: %d" % code_count)
        time_end = time.clock()
        print("用时%d s" % (time_end - time_start))

        a = input()
