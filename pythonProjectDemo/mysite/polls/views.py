from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    myname = 'Võ Duy Việt'
    taisan=['Điện Thoại','Máy tính','xe ware']
    context ={"name": myname,'possession': taisan}
    return render(request,"polls/index.html",context)
