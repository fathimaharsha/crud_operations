from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:task_id1>/',views.Update,name='update'),
]