from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login,logout

# basic attachments 
def home(request):
    return render (request,'index.html')
def services(request):
    return render (request,'services.html')
from django.shortcuts import render, HttpResponse
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Contact form submitted successfully and saved to the database!")
        else:
            # Handle form errors if needed
            return HttpResponse("Contact form submission failed. Please check the form.")
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    
def about(request):
    return render (request,'about.html')

#authentication
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("User saved successfully!")
            user = form.cleaned_data.get('username')
            messages.success(request, user + 'registered successfully!')
            return redirect('login') 
        else:
            print("Form is invalid:", form.errors)
    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context = {'error': 'Invalid login credentials'}
            messages.info(request,'Username or Password is Incorrect!')
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')