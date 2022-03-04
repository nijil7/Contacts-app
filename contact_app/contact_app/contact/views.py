from django.contrib import messages
from django.shortcuts import render,redirect
from .models import contact, reg
# Create your views here.

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        pword = request.POST['pword']
        secret = request.POST['secret']
        if reg.objects.filter(email=email).exists():
                messages.info(request,"Email alredy registered!")
                return render(request,"register.html")
        else:
            member = reg(email=request.POST['email'], pword=request.POST['pword'],secret=request.POST['secret'])
            member.save()
            return redirect('/login/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        if reg.objects.filter(email=request.POST['email'],pword=request.POST['pword']).exists():
            member = reg.objects.get(email=request.POST['email'], pword=request.POST['pword'])
            request.session['uid'] = member.id
            return render(request,'contactlist.html',{'member': member})
        else:
            messages.info(request, "Invalid Credinals")
            return render(request, "login.html")
    else:
        return render(request,'login.html')

def contactlist(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        id = request.session['uid']
        mem = reg.objects.filter(id=id)
        obj = contact(name=name,email=email,number=number,reg_id=mem.id)
        obj.save()
        member = contact.objects.filter(reg_id=id)
        return render(request,'contactlist.html',{'member': member})
    else:
        member = contact.objects.filter(reg_id=id)
        return render(request,'contactlist.html',{'member': member})