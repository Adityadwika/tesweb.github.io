from django.shortcuts import render

def index(request):
    context = {
        'title':'HidhzDev',
        'heading':'Selamat Datang DiWebsite Saya',
    }
    return render(request,'index.html',context)