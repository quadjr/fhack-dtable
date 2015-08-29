from django.shortcuts import render
from django.http import HttpResponse
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


def get_articles(request, scene):
    
    f = json.load(urllib2.urlopen("http://fashionhack.jp/api/search.php?keyword="+scene.encode('utf-8')))
#    obs = json.dumps(f.read(), ensure_ascii=False, indent=4)
#    obs = json.loads(f.read())

    image_urls = []
    for i in range(0,len(f)):
        image_urls.append(f['matches'][i]['document']['fields']['thumbnail'])


    return HttpResponse(image_urls)
#    return HttpResponse(f['matches'][1]['document']['fields']['images'])