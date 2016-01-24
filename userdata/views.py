from django.shortcuts import render
from userdata.form import *
from userdata.models import *
# Create your views here.
def home(request):
    if request.method=="POST":
        cd=request.POST
        t=user.objects.get(email=cd['email'])
        if t:
            if t.password==cd["password"]:
                return render(request,"success.html",{'sform':t})
    else:
        return render(request,"home.html",{'form':login})

def lsignup(request):
    if request.method=="POST":
        data=signup(request.POST)
        if data.is_valid():
            cd=data.cleaned_data#The data is encoded to a single format that is unicode
            user.objects.create(email=cd['semail'],username=cd['username'],first_name=cd['first_name'],last_name=cd['last_name'],password=cd['spassword'],dob=cd['dob'])
            return HttpResponseRedirect("/")
    else:
        return render(request,"signup.html",{'sform':signup})
