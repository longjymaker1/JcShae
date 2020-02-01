from django.shortcuts import render
from django.http import HttpResponse
from .models import Central, Provinces, Article, Article_type, City
import json


def Hello_world(request):
    return HttpResponse("Hello World!!")


def index(request):
    if request.method == "GET":
        dongbei = Central.objects.get(central_name='东北').cen_province.all()  # 获取东北省份
        huabei = Central.objects.get(central_name='华北').cen_province.all()  # 华北省份
        huazhong = Central.objects.get(central_name='华中').cen_province.all()  # 华中省份
        huadong = Central.objects.get(central_name='华东').cen_province.all()  # 华东
        huanan = Central.objects.get(central_name='华南').cen_province.all()  # 华南
        xibei = Central.objects.get(central_name='西北').cen_province.all()  # 西北
        xinan = Central.objects.get(central_name='西南').cen_province.all()  # 西南
        quanguo = Central.objects.get(central_name='全国').cen_province.all()  # 全国
        haiwai = Central.objects.get(central_name='海外').cen_province.all()  # 海外
        top_create_article = Article.objects.order_by("-create_time").all()[:5]  # 新上传
        top_like_article = Article.objects.order_by("-like_num").all()[:5]  # 点赞最多
        # 分类信息
        loufeng = Article.objects.filter(article_type_id=2).order_by("-create_time")[:5]  # 楼凤
        bast_art = Article.objects.filter(article_type_id=20).order_by("-create_time")[:5]  # 精品
        xiyu = Article.objects.filter(article_type_id=3).order_by("-create_time")[:5]  # 洗浴
        jiuduan = Article.objects.filter(article_type_id=4).order_by("-create_time")[:5]  # 酒店会所
        zuyu = Article.objects.filter(article_type_id=6).order_by("-create_time")[:5]  # 足浴发廊
        qq_art = Article.objects.filter(article_type_id=6).order_by("-create_time")[:5]  # 全国QQ群
        # 信息整合
        dongbei_huabei = []
        dongbei_huabei.extend(huabei)
        dongbei_huabei.extend(dongbei)
        huazhong_huadong = []
        huazhong_huadong.extend(huazhong)
        huazhong_huadong.extend(huadong)
        xibei_xinan = []
        xibei_xinan.extend(xibei)
        xibei_xinan.extend(xinan)
        huanan_qita = []
        huanan_qita.extend(huanan)
        huanan_qita.extend(quanguo)
        huanan_qita.extend(haiwai)
        context = {
            "dongbei_huabei": dongbei_huabei,
            "huazhong_huadong": huazhong_huadong,
            "xibei_xinan": xibei_xinan,
            "huanan_qita": huanan_qita,
            "top_create_article": top_create_article,
            "top_like_article": top_like_article,
            "loufeng": loufeng,
            "bast_art": bast_art,
            "xiyu": xiyu,
            "jiuduan": jiuduan,
            "zuyu": zuyu,
            "qq_art": qq_art
        }
        return render(request, "index.html", context=context)


def article_list(request, view_type, article_type, provice_id=0, city_id=0):
    context = {
        "view_type": view_type,
        "article_type": article_type,
        "provice_id": provice_id,
        "city_id": city_id,
    }
    if request.method == "GET":
        provinces = Provinces.objects.all()
        context['provinces'] = provinces
        if provice_id != 0:
            cities = Provinces.objects.get(id=provice_id).pro_city.all()
            context['cities'] = cities
        # 获取列表数据
        pass
        return render(request, "article_list.html", context=context)
    if request.method == "POST":
        print(view_type)
        print(article_type)
        print(provice_id)
        print(city_id)
        context = {
            'result': 'success'
        }
        return HttpResponse(json.dumps(context), content_type='application/json')


def article(request, article_id, provice_id=0, city_id=0):
    return render(request, "article.html")
