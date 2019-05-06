# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Tourism

def tourismdb(request):
    file2 = open("../hotels4/tourism-data.txt")
    for line2 in file2:
        if line2.find("Tourism ID") >= 0:
            continue
        data2 = line2.strip().split("\t")

        id2 = data2[0]
        name2 = data2[1]
        # price2 = data2[2]
        # if price2 == '':
        price2 = "0"
        url2 = data2[2]
        xy2 = data2[3]
        y2 = xy2.split(", ")[0]
        x2 = xy2.split(", ")[1]
        test2 = Tourism(tourismId=int(id2), name=name2,
                        price=float(price2), url=url2,
                        x=x2, y=y2)
        test2.save()
    file2.close()
    return HttpResponse("<p>Data added successfully！</p>")