# coding:"utf-8"

class Output(object):
    def output(self, cont, index):
        img_name = "妞妞"
        fout = open(img_name + str(index) + ".jpg", "wb")
        fout.write(cont)
