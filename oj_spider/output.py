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

        return target_dir

    def mk_problem_dir(self, user_dir, dir_name):
        os.chdir(user_dir)
        target_dir = user_dir + "/" + dir_name
        if os.path.isdir(target_dir):
            os.chdir(target_dir)
        else:
            os.mkdir(target_dir)
            os.chdir(target_dir)
        # os.mkdir(target_dir)
        return target_dir

    def html_output(self, page, parent, file_name):
        #root_dir = os.getcwd()
        #target_dir = root_dir + "//" + report_dict["Pro.ID"]
        """
        if os.path.isdir(target_dir):
            os.chdir(report_dict["Pro.ID"])
        else:
            os.mkdir(target_dir)
            os.chdir(target_dir)
            """
        #print(parent)
        os.chdir(parent)
        with open(file_name, "w+", encoding="utf-8") as f:
            f.write(page)
