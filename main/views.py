from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
import re
# main_app/views.py
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, 'main/index.html')






def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Perform validation
        if not name or not email or not phone or not message:
            messages.error(request, 'All fields are required.')
            return redirect('index')

        if len(name) > 100:
            messages.error(request, 'Name must be less than 100 characters.')
            return redirect('index')

        if not re.match(r'^[a-zA-Z\s]+$', name):
            messages.error(request, 'Name should only contain alphabets and spaces.')
            return redirect('index')

        if not re.match(r'^\d{10}$', phone):
            messages.error(request, 'Phone number should be 10 digits.')
            return redirect('index')

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messages.error(request, 'Invalid email address.')
            return redirect('index')

        # Save the data to the database
        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('index')  # Redirect to the homepage after form submission

    return redirect('index')

# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        print("cannot login",form)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("data is ",username,password)
            user = authenticate(username=username, password=password)
            print("authenticate",user)
            if user is not None:
                print(user)
                login(request, user)
                send_mail(
                   subject="testing",
                  message= "This mail is for the testing purpose .",
                   from_email=settings.EMAIL_HOST_USER,
                   recipient_list=["mekirandahake@gmail.com"],
                 
                   
                )
                
                return redirect('index')  # Replace 'home' with your desired URL after login
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # Replace 'home' with your desired URL after logout

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})
