from django.shortcuts import render

def homeView(request):
    return render(request,'stopkiddingaround.html')
def uploadImageView(request):
    if request.method == "POST":
        dodo = 1;
    else:
        return render(request, "stopkiddingaround.html")