from django.shortcuts import render
import operator

def home(request):
    return render(request,"home.html")

def count(request):
    data=request.GET['fulltextarea']
    data_list=data.split()
    count=len(data_list)

    worddictionary={}

    for word in data_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorted_list=sorted(worddictionary.items(), key = operator.itemgetter(1),reverse=True)

    return render(request,"count.html",{"Full_data":data, "counter":sorted_list})