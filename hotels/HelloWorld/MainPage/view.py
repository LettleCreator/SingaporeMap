from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test, Tourism

def map(request):
    context = {}
    query = request.GET["query"]
    result = []
    result2 = []
    isHotel = True
    LocationXX = [1.292176, 103.858742]
    if query is None or query == '':
        list = Test.objects.all()
        list2 = Tourism.objects.all()
    else:
        print("Fuzzy query")
        list = Test.objects.filter(name__contains=query)
        list2 = Tourism.objects.filter(name__contains=query)
        if(list):
            LocationXX = [float(list[0].x),float(list[0].y)]
            list2 = Tourism.objects.all()
        elif(list2):
            list = Test.objects.all()
            LocationXX = [float(list2[0].x), float(list2[0].y)]
            isHotel = False
    print(len(list))
    for var in list:
        name = var.name
        star = var.star
        price = var.price
        url = var.url
        xy = [float(var.x),float(var.y)]
        obj = {}
        obj["xy"] = xy
        obj["name"] = name
        obj["star"] = "Star: " + star
        obj["price"] = price
        obj["url"] = url
        result.append(obj)
    for var in list2:
        name2 = var.name
        url2 = var.url
        xy2 = [float(var.x),float(var.y)]
        obj_tourism = {}
        obj_tourism["xy"] = xy2
        obj_tourism["name"] = name2
        obj_tourism["url"] = url2
        result2.append(obj_tourism)
    if isHotel:
        context['athlete_list3'] = result
    else:
        context['athlete_list'] = result
    context['athlete_list2'] = result2
    context['query'] = query
    context['hotels'] = list
    context['tourisms'] = list2
    context['zoom'] = 13
    context['LocationXX'] = LocationXX
    return render(request, 'map.html', context)

def hotel(request):
    context = {}
    hotelId = request.GET["hotelId"]
    result = []
    result2 = []
    LocationXX = [1.292176, 103.858742]
    list_tourism = Tourism.objects.all()
    list_hotel = Test.objects.all()
    if hotelId is None or hotelId == '':
        list = list_hotel
    else:
        list = Test.objects.filter(hotelId=hotelId)
        if(list):
            LocationXX = [float(list[0].x), float(list[0].y)]
    for var in list:
        name = var.name
        star = var.star
        price = var.price
        url = var.url
        xy = [float(var.x),float(var.y)]
        obj = {}
        obj["xy"] = xy
        obj["name"] = name
        obj["star"] = "Star: " + star
        obj["price"] = price
        obj["url"] = url
        result.append(obj)
    for var in list_tourism:
        name2 = var.name
        url2 = var.url
        xy2 = [float(var.x),float(var.y)]
        obj_tourism = {}
        obj_tourism["xy"] = xy2
        obj_tourism["name"] = name2
        obj_tourism["url"] = url2
        result2.append(obj_tourism)
    context['athlete_list3'] = result
    context['athlete_list2'] = result2
    context['query'] = ""
    context['hotels'] = list
    context['tourisms'] = list_tourism
    context['zoom'] = 16
    context['LocationXX'] = LocationXX
    return render(request, 'map.html', context)

def tourism(request):
    context = {}
    tourismId = request.GET["tourismId"]
    result = []
    result2 = []
    LocationXX = [1.292176, 103.858742]
    list_tourism = Tourism.objects.all()
    list_hotel = Test.objects.all()
    if tourismId is None or tourismId == '':
        list = list_tourism
    else:
        list = Tourism.objects.filter(tourismId=tourismId)
        if (list):
            LocationXX = [float(list[0].x), float(list[0].y)]
    for var in list_hotel:
        name = var.name
        star = var.star
        price = var.price
        url = var.url
        xy = [float(var.x),float(var.y)]
        obj = {}
        obj["xy"] = xy
        obj["name"] = name
        obj["star"] = "Star: " + star
        obj["price"] = price
        obj["url"] = url
        result.append(obj)
    for var in list:
        name = var.name
        url = var.url
        xy = [float(var.x), float(var.y)]
        obj2 = {}
        obj2["xy"] = xy
        obj2["name"] = name
        obj2["url"] = url
        result2.append(obj2)
    context['athlete_list'] = result
    context['athlete_list2'] = result2
    context['query'] = ""
    context['tourisms'] = list
    context['hotels'] = list_hotel
    context['zoom'] = 16
    context['LocationXX'] = LocationXX
    return render(request, 'map.html', context)