# coding:"utf-8"

class Output(object):
    def output(self, cont, index):
        img_name = "妞妞"
        ss = img_name + str(index) + ".jpg"
        fout = open(ss, "wb")
        fout.write(cont)
