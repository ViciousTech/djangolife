from django.shortcuts import render
from userdata.form import *
from userdata.models import *
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    lerror=[]
    if request.method=="POST":
        l=request.POST
        if ( not l['email'] ) or (not l['password']):
            lerror.append("Fields cannot be left empty")
        if (not '@' in l['email']) or (not '.com' in l['email']):
            lerror.append("Enter a valid email Id")
        if not lerror:
            t=user.objects.get(email=l['email'])
            if t:
                if t.password==l["password"]:
                    return render(request,"alogin.html",{'sform':t})

                else:
                    lerror.append("Password do not match")
            else:
                lerror.append("No such email")
    return render(request,"home.html",{'form':login,'lerror':lerror})

def lsignup(request):
    if request.method=="POST":
        data=signup(request.POST)
        if data.is_valid():
            cd=data.cleaned_data#The data is encoded to a single format that is unicode
            user.objects.create(email=cd['semail'],username=cd['username'],first_name=cd['first_name'],last_name=cd['last_name'],password=cd['spassword'],dob=cd['dob'])
            return HttpResponseRedirect("/")
    else:
        return render(request,"signup.html",{'sform':signup})
