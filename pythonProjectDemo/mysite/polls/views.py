from django.shortcuts import render

from .models import *
# Create your views here.


def index(request):
    myname = 'Võ Duy Việt'
    taisan = ['Điện Thoại', 'Máy tính', 'xe ware']
    context = {"name": myname, 'possession': taisan}
    return render(request, "polls/index.html", context)

def viewList(request):
    list_question = Question.objects.all()
    context1 = {"dsquestions": list_question}
    return render(request, "polls/question_list.html", context1)
