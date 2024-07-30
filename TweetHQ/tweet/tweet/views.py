from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("hello world you are in home page :::")
    return render(request,'tweet_list.html')