from django.shortcuts import render , redirect
from django.views import View
from .forms import CustomUserCreationForm , LoginUserForm
from django.contrib.auth import login , authenticate
from django.contrib import messages
# Create your views here.

class RegisterUserView(View):
    def get(self,request):
        form = CustomUserCreationForm()
        context = {'form' : form }
        return render(request,'accounts/register.html',context)
    
    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'accounts/register.html',{'form' : form})
        
        
        
class LoginUserView(View):
    def get(self,request):
        form = LoginUserForm()
        return render(request , 'accounts/login.html' , {'form' : form})
    
    def post(self,request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request ,email=email , password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,'ایمیل یا گذرواژه نادرست است')
                return render(request , 'accounts/login.html' , {'form' : form})
        else:
            return render(request , 'accounts/login.html' , {'form' : form})