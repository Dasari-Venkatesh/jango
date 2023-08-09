from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("venky",views.venky,name="venky"),
     path("<str:name>", views.greet, name="greet")
    #  path("{name}",views.greet,name="greeet")

 ]