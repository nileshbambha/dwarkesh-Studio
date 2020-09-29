from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import example_models
from django.contrib.auth.models import User , auth
# Create your views here.
def index(request):
    
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    # data = example_models.objects.all()
    # print(data)
    # return render(request,'about.html',{'datas':data})
def portfolio(request):
    data = example_models.objects.all()
    return render(request,'portfolio.html',{'datas':data})
def services(request):
    return render(request,'services.html')
# def registration(request):
#     if request.method == 'POST':
#         user_name = request.POST['user_name']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name'] 
#         # birthday = request.POST['birtday']
#         gender = request.POST['gender']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         password = request.POST['password']

#         users = User.objects.create_user(username =user_name,password = password,first_name = first_name,last_name = last_name,email=email)
#         users.save();
#         return redirect('/')
#     else:
#         return render(request,'registration_form.html')
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        
        users =auth.authenticate(request,username=name,password=password)

        if users is not None:
            auth.login(request,users)
            return redirect('/')
        else:
            print("invalic username password")
            return redirect('login')
    else:
        return render(request,'login.html')
# def logout(request):
#     auth.logout(request)
#     return redirect('index.html')
def contact(request):
     return render(request,'contact.html')
# def blog(request):
#     return render(request,'blog.html')
# def elements(request):
#     return render(request,'elements.html')
def portfolio_details(request):
    return render(request,'portfolio_details.html')
# def single_blog(request):
#     return render(request,'single-blog.html')
