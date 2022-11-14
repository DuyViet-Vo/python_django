from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.views import View
from django.template.response import TemplateResponse
# Create your views here.
class IndexClass(View):
    def get(self,request):
        ketqua= '123123asfdgsa'
        return HttpResponse(ketqua)
class PostClass(View):
    def get(self,request):
        a = PostForm()
        return render(request,"news/add_news.html",{'f': a})

class ClassSaveNews(View):
    def post(self,request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return  HttpResponse('Luw Thanh Cong!')
        else:
            return HttpResponse('Loi Validate')

def email_view(requset):
    b = SendEmail()
    return  render(requset,'news/email.html',{'f': b})

def process(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            tieude = m.cleaned_data['title']
            cc = m.cleaned_data['cc']
            noidung= m.cleaned_data['content']
            email = m.cleaned_data['email']
            context ={ 'td':tieude,'c':cc,'nd':noidung,'e':email }
            return render(request,'news/print_email.html',context)
        else:
            return HttpResponse("form not validate")
    else:
        return HttpResponse('khong phai POST method')