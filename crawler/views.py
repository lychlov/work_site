from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("This is index")


def target_mps(request):
    return HttpResponse("show targetmps")


def query_detail(request, query_dict):
    return HttpResponse('show querys & details')


def detail(request, target_mp_name):
    return HttpResponse('show details')
