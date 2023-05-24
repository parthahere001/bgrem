from io import BytesIO
from django.shortcuts import render, redirect
from rembg import remove
from PIL import Image
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from .models import imageStorageModel
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def homeView(request):
    return render(request,'home.html')

@csrf_exempt
def uploadImageView(request):
    if request.method == "POST":
        try:
            pic = request.FILES['fileUpload']
            response = HttpResponse(content_type="image/png")
            input = Image.open(pic)
            output = remove(input)
            fordb = output
            img_io = BytesIO()
            fordb.save(img_io, format='png', quality=100)
            img_content = ContentFile(img_io.getvalue(), 'img.png')
          
            sampl = imageStorageModel(uploaded_image = pic, downloaded_image = img_content)
            sampl.save()
            output.save(response, 'png')
            return response
        except MultiValueDictKeyError:
            return render(request, "stopkiddingaround.html")
    else:
        return render(request, "stopkiddingaround.html")