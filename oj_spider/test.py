year_list = [y for y in range(2013, 2017)]
month_list = []
s = ""
for m in range(1, 13):
    if m < 10:
        s = "0" + str(m)
    else:
        s = str(m)
    month_list.append(s)
    #print(s)
date_list = [str(y) + "-" + str(m)
             for y in year_list for m in month_list]
date_dict = {}
for d in date_list:
    date_dict[d] = ""
    print(d)
