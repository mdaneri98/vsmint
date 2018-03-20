from django.shortcuts import render
from django.http import HttpResponse
from django import views

# Create your views here.
class Home(views.View):

    def get(self, request):
        


        return HttpResponse("Todo ok!")