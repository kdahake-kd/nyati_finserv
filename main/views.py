from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'main/index.html')




import re

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

