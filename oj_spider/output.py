import os

"""
    用户名(姓名)做根文件夹
    根文件夹里面有一份根据所有提交过的代码总结出来的实验报告
    以题号作为一个文件夹,放在根文件夹里面.里面有提交过的文本文件,还有一份这个题号的总结报告

"""


class Output(object):

    def mk_root_dir(self, name):
        root_dir = os.getcwd()
        target_dir = root_dir + "//" + name
        if os.path.isdir(target_dir):
            os.chdir(target_dir)
        else:
            os.mkdir(target_dir)
            os.chdir(target_dir)

    def html_output(self, page, report_dict, dir):
        root_dir = os.getcwd()
        target_dir = root_dir + "//" + report_dict["Pro.ID"]
        if os.path.isdir(target_dir):
            os.chdir(report_dict["Pro.ID"])
        else:
            os.mkdir(target_dir)
            os.chdir(target_dir)
        with open(report_dict["Run.ID"] + ".cpp", "w+", encoding="utf-8") as f:
            f.write(page)
        os.chdir(dir)
