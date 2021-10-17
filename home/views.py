from django.shortcuts import render, HttpResponse
from home.models import Register


# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def mapview(request):
    return render(request, 'mapview.html')
def regi(request):
    if request.method=="POST":
        first=request.POST['first']
        last=request.POST['last']
        email=request.POST['email']
        depa=request.POST['depa']
        cor1x= request.POST['cor1x']
        cor1y= request.POST['cor1y']
        cor1st=request.POST['cor1st']
        cor1ed=request.POST['cor1ed']
        rate1= request.POST['rate1']
        reason1=request.POST['reason1']
        cor2x= request.POST['cor2x']
        cor2y= request.POST['cor2y']
        cor2st=request.POST['cor2st']
        cor2ed=request.POST['cor2ed']
        rate2= request.POST['rate2']
        reason2=request.POST['reason2']
        cor3x= request.POST['cor3x']
        cor3y= request.POST['cor3y']
        cor3st=request.POST['cor3st']
        cor3ed=request.POST['cor3ed']
        rate3= request.POST['rate3']
        reason3=request.POST['reason3']
        gender=request.POST['gender']
        age=request.POST['age']
        trans=request.POST['trans']
        res=Register(first=first,last=last,email=email,depa=depa,cor1x=cor1x,cor1y=cor1y,cor1st=cor1st,cor1ed=cor1ed
        ,rate1=rate1,reason1=reason1,cor2x=cor2x,cor2y=cor2y,cor2st=cor2st,cor2ed=cor2ed,rate2=rate2,reason2=reason2,
        cor3x=cor3x,cor3y=cor3y,cor3st=cor3st,cor3ed=cor3ed,rate3=rate3,reason3=reason3,gender=gender,age=age,trans=trans)
        res.save()
    return render(request, 'register.html')