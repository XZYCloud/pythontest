# from django.http import HttpResponse
from django.shortcuts import render
from xzy.getmovies import get_all
from xzy.models import Douban


def top250(request):
    if Douban.objects.count()==0:
        #数据库没有数据时，即第一次运行时传递我们爬取的信息
        savemovies=get_all()
        for i in savemovies:
            addtion=Douban(num=i['num'],name=i['name'],charactor=i['charactor'],\
                           remark=i['remark'],score=i['score'])
            addtion.save()

    html_data=Douban.objects

    return render(request,'top250.html',{'html_data':html_data})