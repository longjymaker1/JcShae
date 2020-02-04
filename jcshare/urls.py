from django.urls import re_path,path
from . import views


urlpatterns = [
    path('Hello_world', views.Hello_world, name='Hello_world'),
    path('', views.index, name='index'),
    # path('publish/t', views.article_list),
    re_path(r"^(?P<view_type>publish)/(?P<article_type>\w+)$", views.article_list),
    re_path(r"^(?P<view_type>like)/(?P<article_type>\w+)$", views.article_list),
    re_path(r"^(?P<view_type>view)/(?P<article_type>\w+)$", views.article_list),
    re_path(r"^(?P<view_type>comment)/(?P<article_type>\w+)$", views.article_list),

    re_path(r'^(?P<view_type>publish)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)$', views.article_list),
    re_path(r'^(?P<view_type>like)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)$', views.article_list),
    re_path(r'^(?P<view_type>view)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)$', views.article_list),
    re_path(r'^(?P<view_type>comment)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)$', views.article_list),

    re_path(r'^(?P<view_type>publish)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>like)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>view)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>comment)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)$',
            views.article_list),

    re_path(r"^(?P<view_type>publish)/(?P<article_type>\w+)/page/(?P<page_num>\d+)$", views.article_list),
    re_path(r"^(?P<view_type>like)/(?P<article_type>\w+)/page/(?P<page_num>\d+)$", views.article_list),
    re_path(r"^(?P<view_type>view)/(?P<article_type>\w+)/page/(?P<page_num>\d+)$", views.article_list),
    re_path(r"^(?P<view_type>comment)/(?P<article_type>\w+)/page/(?P<page_num>\d+)$", views.article_list),

    re_path(r'^(?P<view_type>publish)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/page/(?P<page_num>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>like)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/page/(?P<page_num>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>view)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/page/(?P<page_num>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>comment)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/page/(?P<page_num>\d+)$',
            views.article_list),

    re_path(r'^(?P<view_type>publish)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)/page/(?P<page_num>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>like)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)/page/(?P<page_num>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>view)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)/page/(?P<page_num>\d+)$',
            views.article_list),
    re_path(r'^(?P<view_type>comment)/(?P<article_type>\w+)/provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)/page/(?P<page_num>\d+)$',
            views.article_list),

    re_path(r'^provice/(?P<provice_id>\d+)/city/(?P<city_id>\d+)/article_page/(?P<article_id>\d+)$', views.article),
]