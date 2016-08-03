#!/usr/bin/env python
# encoding:utf-8
from django.conf.urls import url 
from . import views 

# urlpatterns = [
# 	url(r'^$', views.post_list,name='post_list'),
# 	url(r'^(?P<post_id>\d)/$',views.post_detail,name='post_detail'),
# 	## 使用(?P<>\d+)的形式捕获值给<>中得参数，比如(?P<article_id>\d+)，
# 	#当访问/blog/article/3时，将会将3捕获给article_id,这个值会传到
# 	#views.ArticleDetailView,这样我们就可以判断展示哪个Article了
# ]

# 优化URL

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    # url(r'^(?P<post_id>\d)/$', views.post_detail, name='post_detail'),
    url(r"^(?P<post_id>\d+)/share/$", views.post_share, name='post_share'),
]