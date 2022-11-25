from django.contrib.auth import authenticate
from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth.models import User
# Create your views here.
class IndexClass(View):
    def get(self,request):
        return HttpResponse('<h1>Xin Chao</h1>')

class LoginClass(View):
    def get(self,request):
        return render(request,template_name='Login/login.html')

    def post(self,request):
        user_name = request.POST.get('tendangnhap')
        matkhau = request.POST.get('matkhauu')
        my_user= authenticate(username=user_name,password = matkhau)
        if my_user is None:
            return HttpResponse('user khong ton tai')
        return HttpResponse('ban vua dang  nhap %s %s'%(user_name,matkhau))