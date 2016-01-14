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

    def data_output(self,content,dir):
        os.chdir(dir)
        print(os.getcwd())
        with open("ai1.txt","r",encoding="utf-8") as f:
            s = f.read() + "\n"
        with open("report_temp.html","w",encoding = "utf-8") as f:
            f.write(s)
            f.write(".num0{background-color:#333333;height:")
            #content[0] = str(content[0])
            print(content[0])
            f.write(content[0])
            f.write("px;}\n")

            f.write(".num1{background-color:#333333;height:")
            #content[1] = str(content[1])
            f.write(content[1])
            f.write("px;}\n")

            f.write(".num2{background-color:#990099;height:")
            #content[2] = str(content[2])
            f.write(content[2])
            f.write("px;}\n")

            f.write(".num3{background-color:#990099;height:")
            #content[3] = str(content[3])
            f.write(content[3])
            f.write("px;}\n")

            f.write(".num4{background-color:#00A000;height:")
            #content[4] = str(content[4])
            f.write(content[4])
            f.write("px;}\n")

            f.write(".num5{background-color:#00A000;height:")
            #content[5] = str(content[5])
            f.write(content[5])
            f.write("px;}\n")
        with open("ai2.txt","r",encoding="utf-8") as f:
            s = f.read()
        with open("report_temp.html","a+",encoding="utf-8") as f:
            f.write(s)
