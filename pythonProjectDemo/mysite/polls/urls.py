from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.viewList, name="View_list"),
    path('',views.index,name= "index" ),
]