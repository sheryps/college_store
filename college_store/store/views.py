from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Department,Course,User_details
from django.utils.safestring import mark_safe
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def home(request):
    department=Department.objects.all()
    context={'departments':department}
    return render(request,'home.html',context)

def load_courses(request):
    department_id=request.GET.get('department')    
    courses=Course.objects.filter(department_id=department_id).order_by('course')
    return render(request,'load_courses.html',{'courses':courses})

def details(request):
    if request.method=='POST':
        user=request.user.id
        name = request.POST['name']
        age = request.POST['age']
        dob = request.POST['dob']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['Address']
        department=request.POST['dept']
        course = request.POST['course']
        purpose = request.POST['purpose']
        try:
            Notebook = request.POST['notebook']
            pen = request.POST['pen']
            exam_Pappers = request.POST['exam Pappers']
            Materials = [Notebook,pen,exam_Pappers]
        except:
            pass
        student=User_details(user_id=user,Name=name,Age=age,DOB=dob,Gender=gender,phone=phone,Email=email,Address=address,Department=department,
        course=course,purpose=purpose)    
        student.save()    
        messages.info(request, mark_safe("Order Confirmed.<a href='/'>Return to Homepage</a>"))            
        return redirect('home')    

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print('welcome')
            auth.login(request,user)
            return redirect('home')
    return render(request,'login.html')    

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        confirm = request.POST['confirm']
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User already exists')
                return redirect('register')
            else:    
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matching')        
        return redirect('register')
    return render(request,'register.html')        

@login_required(login_url='login')  
def logout(request):
    auth.logout(request)
    return redirect('/')    