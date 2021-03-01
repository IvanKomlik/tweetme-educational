from json.encoder import JSONEncoder
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tweets.models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")

def tweet_detail_view(reqest, tweet_id, *args, **kwargs):
    
    tweet_from_query = Tweet.objects.get(id=tweet_id)

    data = {
        "id": tweet_from_query.id,
        "content": tweet_from_query.content
    }
    return JsonResponse(data=data)

