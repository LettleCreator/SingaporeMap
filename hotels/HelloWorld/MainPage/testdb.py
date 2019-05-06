# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# http://127.0.0.1:8000/testdb
def testdb(request):
    file = open("../hotel-data.txt")
    for line in file:
        if line.find("Hotel ID") >= 0:
            continue
        data = line.strip().split("\t")

        id = data[0]
        name = data[1]
        price = data[2]
        if price == '':
            price = "0"
        url = data[3]
        xy = data[4]
        x = xy.split(", ")[0]
        y = xy.split(", ")[1]
        star = data[5]
        test1 = Test(hotelId=int(id), name=name,
                     star=star, price=float(price),
                     url=url,
                     x=x, y=y)
        test1.save()
    file.close()
    return HttpResponse("<p>Data added successfully！</p>")
