from django.http import HttpResponse
from django.shortcuts import render
from cropperjs.models import CropperImageField
import json
# class opened_image:
#     url


def default(request):
    image_field = CropperImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    return HttpResponse("HELLO")
def hello(request):
    return render(request,r"image.html")
def image(request,handlername):
    absfilepath = '/imagesource/image/' + handlername +'.png'
    return render(request,r"image.html",{'filename':absfilepath})
def imagesjs(request,handlername):

    with open('./static/json/'+handlername+'.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
        return render(request, r"image2.html", {'jsondata': json.dumps(data)})

