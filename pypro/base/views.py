from django.http import HttpResponse
from django.shortcuts import render # noqa

# Create your views here.


def home(request):
    return HttpResponse("Para de enrolar Bozex e aperta logo esse carai!!!")
