from django.shortcuts import render,redirect
from django.views import View
from auth import forms
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
class Login(LoginView):
    template_name='auth/login.html'

class logout(LogoutView):
    pass
class signup(View):
    def get(self,request):
        context={
         "form":forms.SignupForm()
        }
        return render(request,'auth/signup.html',context)
    def post(self,request):
        form=forms.SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            
            return redirect('/')
        context={
         "form":form
        }
        return render(request,'auth/signup.html',context)    

# Create your views here.
