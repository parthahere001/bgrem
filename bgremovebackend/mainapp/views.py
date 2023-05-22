from django.shortcuts import render, redirect
from rembg import remove
from PIL import Image
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def homeView(request):
    return render(request,'home.html')
def uploadImageView(request):
    if request.method == "POST":
        try:
            pic = request.FILES['fileUpload']
            response = HttpResponse(content_type="image/png")
            input = Image.open(pic)
            output = remove(input)
            output.save(response,'png')
            return response
        except MultiValueDictKeyError:
            return render(request, "stopkiddingaround.html")
    else:
        return render(request, "stopkiddingaround.html")