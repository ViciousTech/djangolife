import bcrypt
from django.shortcuts import render
from userdata.form import *
from userdata.models import *
from django.http import HttpResponseRedirect
from django.db.models import Max


def home(request):
    lerror=[]
    if request.method=="POST":
        l=request.POST
        if ( not l['email'].strip() ) or (not l['password'].strip()):
            lerror.append("Fields cannot be left empty")
        if not lerror:
            t=user.objects.get(email=l['email'])
            if t:
                if bcrypt.hashpw(str(l['password']),str(t.password)) == str(t.password):
                    return render(request,"alogin.html",{'sform':t})
                else:
                    lerror.append("Password do not match")
            else:
                lerror.append("No such email")
    return render(request,"home.html",{'form':login,'lerror':lerror})

def lsignup(request):
    serror=[]
    if request.method=="POST":
        data=signup(request.POST)
        if data.is_valid():
            cd=data.cleaned_data#The data is encoded to a single format that is unicode
            try:#making sure accounts are not redundant
                email_check = user.objects.get(email = cd['semail'] )
                user_check = user.objects.get(username = cd['username'])
            except:
                email_check = []
                user_check = []
            for i in user_check:
                serror.append("Username already in use")

            for i in email_check:
                serror.append("Email already in use")
            if(cd['spassword'] != cd['cf_password']):
                serror.append("Passwords do not match")
            if not serror:
                salt = bcrypt.gensalt(14)
                vericode = salt[7:]
                hashed_pass = bcrypt.hashpw(str(cd['spassword']),salt)
                id = user.objects.all().aggregate(Max('user_id'))
                if id['user_id__max'] is None : userid = 0
                else: userid = int(id['user_id__max']) + 1
                user.objects.create(user_id = userid ,email=cd['semail'],username=cd['username'],first_name=cd['first_name'],last_name=cd['last_name'],password=hashed_pass,dob=cd['dob'])
                return HttpResponseRedirect("/")
            else:
                return render(request,'signup.html',{'sform':signup,'serror':serror})
    else:
        return render(request,'signup.html',{'sform':signup,'serror':serror})
