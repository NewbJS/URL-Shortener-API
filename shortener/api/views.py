from django.http.response import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import URLInfo
import string
import random

@csrf_exempt
def make_short(request):
    
    if request.method == "POST":
        param_url = request.POST.get('long_url', False)
        chars = string.ascii_letters
        short_url = ''.join(random.sample(chars, k=5))
        
    
        x = list(URLInfo.objects.filter(long_url=param_url))
        
        if x:
            short_url = x[0].short_url
        
        else:
            new_url = URLInfo(long_url=param_url, short_url=short_url)
            new_url.save()

        json = {
            "short_url": short_url,
            "long_url": param_url,
        }

        return JsonResponse(json)
    else:

        return HttpResponseBadRequest()


@csrf_exempt
def get_long(request, short_url):

    if request.method == "GET":
        obj = URLInfo.objects.filter(short_url=short_url)
        res = HttpResponse(status=301)
        res["location"] = obj[0].long_url
        return res
    else:
        return HttpResponseBadRequest()