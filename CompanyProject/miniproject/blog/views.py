from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
# Home View. 
def home(request):
    return render (request, 'blog/home.html')

# Dashboard
def dashboard(request):
    return render (request, 'blog/dashboard.html')

#logout
def user_logout(request):
   return HttpResponseRedirect('/');




#SignUp
def user_signup(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST)
  if form.is_valid():
   messages.success(request,'Congratulations !! You Have Sucessully Register plz login')
   form.save()
 else:
  form = UserCreationForm()
 return render (request, 'blog/signup.html' ,{'form':form})
 
 #Login
def user_login(request):

 form=AuthenticationForm() 
 return render (request, 'blog/login.html',{'form':form})