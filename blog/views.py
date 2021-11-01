from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Blog',
        'heading':'Selamat Datang Dihalaman Blog Saya'
    }
    return render(request,'blog/index.html',context),