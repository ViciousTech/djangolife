from django.shortcuts import render
from userdata.form import *
# Create your views here.
def home(request):
    return render(request,"home.html",{'form':login})
