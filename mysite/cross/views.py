from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

import urllib
import urllib2
import json


# 
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, 'http://fashionhack.jp/api/', 'tfhjp', 'tanoshiine')

# 
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_articles(request, keyword):
    
    f = json.load(urllib2.urlopen("http://fashionhack.jp/api/search.php?keyword="+keyword.encode('utf-8')))
    image_urls = []
    for i in range(0,len(f)):
        image_urls.append(f['matches'][i]['document']['fields']['thumbnail'])

    context = {'image_urls' : image_urls}
    return render(request, 'cross/get_articles.html', context)

#    return HttpResponse(image_urls)



def article_detail(request, keyword, id):
    
    f = json.load(urllib2.urlopen("http://fashionhack.jp/api/search.php?keyword="+keyword.encode('utf-8')))


    id = int(id)
    
    dic = {}
    dic['image_url'] = f['matches'][id]['document']['fields']['thumbnail']
    dic['magazinename'] = f['matches'][id]['document']['fields']['magazinename']
    dic['month'] = f['matches'][id]['document']['fields']['month']
    dic['publisher'] = f['matches'][id]['document']['fields']['publisher']
    dic['text'] = f['matches'][id]['document']['fields']['text_shingle2']

    context = {'article_info' : dic}
    return render(request, 'cross/article_detail.html', context)

