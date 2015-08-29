from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_articles/(?P<keyword>.+)$', views.get_articles, name='get_articles'),
    url(r'^article_detail/(?P<keyword>.+)/(?P<id>[0-9]+)$', views.article_detail, name='les'),
    url(r'^get_items/(?P<scene>.+)$', views.get_articles, name='get_items'),
]
