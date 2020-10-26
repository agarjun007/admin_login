from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import cards
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect(home)    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request,user)
            return JsonResponse('valid', safe=False)
        else:
            return JsonResponse('invalid', safe=False)
    else:
        return render(request,'index.html')
    
def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return JsonResponse('usernamemismatch',safe=False)
                
                # return redirect('/')
            else: 
                user = User.objects.create_user(first_name=name,username=username,email=email,password = password1)
                user.save();
            messages.info(request, "User created successfully..")    
            return JsonResponse('valid', safe=False)       
        else:
            return JsonResponse('invalid', safe=False)
            # messages.info(request,"password not match")    
    else:    
        return render(request,'signup.html')

def home(request):
    obj1 = cards()
    obj1.img = 'https://b.zmtcdn.com/data/dish_photos/ed0/78894e7c88854f29b80493101f916ed0.jpg'
    obj1.item = 'Chicken Biriyani'
    obj1.desc = 'Top sellers Paramount, Nehdi and Zam Zam'
    obj1.price = 120
    
    obj2 = cards()
    obj2.img = 'https://i.ytimg.com/vi/HVi7xxQZDRQ/maxresdefault.jpg'
    obj2.item = 'Alfam'
    obj2.desc = 'Top sellers Nehdi , Buhari and Zam Zam'
    obj2.price = 240
    
    obj3 = cards()
    obj3.img = 'https://i.ytimg.com/vi/WBXgmNkyMz4/maxresdefault.jpg'
    obj3.item = 'Kuzhimanthi'
    obj3.desc = 'Top sellers Nehdi,Buhari and Rahmath '
    obj3.price = 150
    objects=[obj1,obj2,obj3]

    if request.user.is_authenticated:
        return render(request,'home.html',{'objects':objects} )
       
    else:
        return redirect(login)

    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.info(request, "Logged out Successfully")
        return redirect(login)

def adminlogin(request):
    if request.session.has_key('password'):
        return redirect(adminpanel)  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'arjun@gmail.com' and password == '12345':
            request.session['password'] = password
            table = User.objects.all().order_by ('date_joined')
            return render(request,'adminpanel.html',{'table_data':table})
        else:
            return redirect('/adminlogin')
    else:
       return render(request,'adminlogin.html')

      

def adminpanel(request): 
    
    if request.session.has_key('password'):
        table = User.objects.all().order_by ('date_joined')
        return render(request,'adminpanel.html',{'table_data':table})
    else:
        return redirect(adminlogin) 

def adminlogout(request):
    if request.session.has_key('password'):
        request.session.flush()
    return redirect(adminlogin)    


def delete(request,id):
    user = User.objects.get(id=id) 
    user.delete()
    return redirect(adminpanel)

def edit(request,id):
    if request.session.has_key('password'):
        user = User.objects.get(id=id) 
        return render(request,'update.html',{'user':user})    
    else:
        return redirect(adminlogin)
def update(request,id):
    if request.session.has_key('password'):
        if request.method=="POST":
            username = request.POST['username']
            email = request.POST['email']
            name = request.POST['name']
            number = User.objects.get(id=id)
            number.email = email
            number.username = username
            number.first_name = name
            number.save()
        
            return redirect(adminpanel)
        else:
        
            return render(request,'update.html')
    else:
        return redirect(adminlogin)           

def create(request):
    if request.session.has_key('password'):
        if request.method == 'POST':
        
            username = request.POST['username']
            name = request.POST['name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    return JsonResponse('usernamemismatch',safe=False)
                elif User.objects.filter(email=email).exists():
                    return JsonResponse('emailmismatch',safe=False)    
                    # return redirect('/')
                else: 
                    user = User.objects.create_user(first_name=name,username=username,email=email,password = password1)
                    user.save();
                messages.info(request, "User created successfully..")
                return JsonResponse('valid', safe=False)       
            else:
                return JsonResponse('invalid', safe=False)
                # messages.info(request,"password not match")    
        else:   
        
            return render(request,'create.html')    
    else:
        return redirect(adminlogin)    
