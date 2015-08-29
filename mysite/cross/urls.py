from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_articles/(?P<scene>.+)$', views.get_articles, name='get_articles'),
    url(r'^get_items/(?P<scene>.+)$', views.get_articles, name='get_items'),
]
