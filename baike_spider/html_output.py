# coding:utf8
class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        fout = open("output.html", "w", encoding="utf-8")

        fout.write("<html>\n")
        fout.write("<body>\n")
        fout.write("<table>\n")
        for data in self.datas:
            # print("()()",type(data["title"]))
            fout.write("<tr>\n")
            fout.write("<td>%s</td>"%data["url"])
            fout.write("<td>%s</td>"%data["title"])
            fout.write("<td>%s</td>"%data["summary"])
            fout.write("</tr>\n")
        fout.write("</table>\n")
        fout.write("</body>\n")
        fout.write("</html>\n")


        fout.close()