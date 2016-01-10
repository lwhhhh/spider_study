"""
    以题号做一个文件夹,里面存放改题交过的代码一份改题的提交报告
"""

from bs4 import BeautifulSoup
import re


class Parser(object):

    def __init__(self):
        pass

    def get_userhome_link(self, page):
        soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")
        tag = soup.find(
            "a", href=re.compile(r"/oj/author/userdata?"))
        user_link = tag.get("href")
        user_link = "http://172.21.85.56" + user_link
        return user_link

    def get_problem_links(self, page):
        soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")
        problem_links = []
        tags = soup.find_all(
            "a", href=re.compile(r"/oj/exercise/status\?author=201424133254&problem_id"))

        for tag in tags:
            tlink = "http://172.21.85.56" + tag.get("href")
            problem_links.append(tlink)

        return problem_links

    def get_next_link(self, page):
        soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")
        tag = soup.find(
            "a", href=re.compile(r"top"))
        next_url = "http://172.21.85.56" + tag.get("href")
        # print(next_url)
        return next_url

    # 未完成多页的情况处理
    def get_code_links(self, page):
        code_links = []
        soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")
        tags = soup.find_all(
            "a", target="_blank", href=re.compile(r"/oj/exercise/sourcecode\?status_id="))
        if tags is None:
            return
        for tag in tags:
            tlink = "http://172.21.85.56" + tag.get("href")
            code_links.append(tlink)
            # print(tlink)

    # 未完成多页的情况处理
    def get_report(self, page):
        count_dict = {"ac": 0, "re": 0, "wa": 0, "tle": 0, "wait": 0, "ce": 0}
        repotr_dict = {}
        page_next = False
        soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")
        tags = soup.find("tbody", id="statusList")
        res = []
        if tags == None:
            return
        for child_tag in tags.children:
            # print(child_tag)
            line = ""
            count = 0
            excute_dict = {}
            run_id = ""
            for s in child_tag.strings:
                # 记录运行信息
                if count == 0:
                    excute_dict["Run.ID"] = s
                    run_id = s
                elif count == 2:
                    excute_dict["Pro.ID"] = s
                elif count == 3:
                    excute_dict["Status"] = s
                elif count == 4:
                    excute_dict["Exe.Time"] = s
                elif count == 5:
                    excute_dict["Exe.Memory"] = s
                elif count == 6:
                    excute_dict["Language"] = s
                elif count == 7:
                    excute_dict["Code Len"] = s
                    # excute_dict["code_url"] = child_tag.get("hr")
                elif count == 8:
                    excute_dict["Submit Time"] = s

                # 记录此页面中代码运行结果情况
                if s == "Accepted":
                    count_dict["ac"] = count_dict["ac"] + 1
                elif s == "Compilation Error":
                    count_dict["ce"] = count_dict["ce"] + 1
                elif s == "Waiting":
                    count_dict["wait"] = count_dict["wait"] + 1
                elif s == "Wrong Answer":
                    count_dict["wa"] = count_dict["wa"] + 1
                elif s == "Runtime Error":
                    count_dict["re"] = count_dict["re"] + 1

                line = line + s + " "
                count = count + 1

            count1 = 0
            soup1 = BeautifulSoup(
                child_tag.prettify(), "html.parser", from_encoding="utf-8")
            code_url = "http://172.21.85.56" + \
                soup1.find(
                    "a", href=re.compile(r"/oj/exercise/sourcecode")).get("href")
            # print(url)
            excute_dict["code_url"] = code_url
            repotr_dict[run_id] = excute_dict
            line = line + "\n"
            res.append(line)

        # for key in count_dict:
            # print(key, ":", count_dict[key])
            for key in repotr_dict:
                pass
                #print(key, ":", repotr_dict[key])

        next_page_link = self.get_next_link(page)
        return repotr_dict, next_page_link

    # 获取页面的代码
    def get_codes(self, page):
        soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")
        tags = soup.find("pre")
        code = tags.get_text()
        return code
