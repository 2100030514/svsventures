from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate

from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')