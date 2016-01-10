import os


class Output(object):

    def html_output(self, page, report_dict, dir):
        root_dir = os.getcwd()
        target_dir = root_dir + "//" + report_dict["Pro.ID"]
        if os.path.isdir(target_dir):
            os.chdir(report_dict["Pro.ID"])
        else:
            os.mkdir(target_dir)
            os.chdir(target_dir)
        with open(report_dict["Run.ID"] + ".txt", "w+", encoding="utf-8") as f:
            f.write(page)
        os.chdir(dir)
