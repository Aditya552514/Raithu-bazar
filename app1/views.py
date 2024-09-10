from django.shortcuts import render,redirect
from .models import Register

def modify(request):
    operation=request.GET['operation']
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    desig=request.GET['desig']
    r=Register.objects.get(email=email)
    if operation=="update":    
        r.fullname=fullname
        r.email=email
        r.password=password
        r.desig=desig
        r.save()
    else:
        Register.delete(r)
    users=Register.objects.all()
    return render(request,"viewusers.html",{"users":users})

def viewusers(request):
    #all() method returns all rows as Register class objects
    users=Register.objects.all()
    return render(request,"viewusers.html",{"users":users})



def index(request):
    return render(request,'layout.html')

def about(request):
    return render(request,'about.html')

def order(request):
    return render(request,'order.html')

def recipes(request):
    return render(request,'recipes.html')
def register (request):
    return render(request,'register.html') 
def login(request):
    return render(request,'login.html')
def Home(request):
    return render(request,'Home.html') 
def dietplan(request):
    return render(request,'dietplan.html')

def a(request):
    return render(request,'a.html')
def b(request):
    return render(request,'b.html')
def c(request):
    return render(request,'c.html')
def d(request):
    return render(request,'d.html')
def e(request):
    return render(request,'e.html')
def f(request):
    return render(request,'f.html')
def g(request):
    return render(request,'g.html')
def h(request):
    return render(request,'h.html')
def order2(request):
    return render(request,'order2.html')
def order3(request):
    return render(request,'order3.html')
def order4(request):
    return render(request,'order4.html')
def order5(request):
    return render(request,'order5.html')
def order6(request):
    return render(request,'order6.html')
def order7(request):
    return render(request,'order7.html')
def order8(request):
    return render(request,'order8.html')
def bc(request):
    return render(request,'bc.html')
def bd(request):
    return render(request,'bd.html')
def be(request):
    return render(request,'be.html')
def bf(request):
    return render(request,'bf.html')
def bg(request):
    return render(request,'bg.html')
def doregister(request):
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    #creating object for Register class
    r=Register()
    #storing local variable values into object
    r.fullname=fullname
    r.email=email
    r.password=password
    r.save()
    return render(request,'Home.html')

