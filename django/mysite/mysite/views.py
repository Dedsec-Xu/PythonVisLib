from django.http import HttpResponse
from django.shortcuts import render 
# class opened_image:
#     url


def default(request):
    return HttpResponse("HELLO") 
def hello(request):
    return render(request,r"image.html")