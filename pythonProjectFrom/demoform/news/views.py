from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.template.response import TemplateResponse
# Create your views here.
def index(request):
    return HttpResponse('xin chao!')

def add_post(request):
    a = PostForm()
    return render(request,"news/add_news.html",{'f': a})

def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return  HttpResponse('Luw Thanh Cong!')
        else:
            return HttpResponse('Loi Validate')
    else:
        return HttpResponse('Khong phai POST request!')