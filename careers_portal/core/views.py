from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import UserProfile
from django.core.exceptions import ValidationError
import re

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .models import UserProfile

def Register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        type=request.POST.get('user_type')
        print(type)
        # Check if email already exists
        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'Register.html')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Register.html')

        # If everything is valid, create a new user profile
        user_profile = UserProfile(phone_number=phone_number, email=email, password=password,type=type)
        user_profile.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')  # Redirect to the login page

    return render(request, 'Register.html')


from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from .models import UserProfile  # Or 'User' if using the default model

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        # Check if email and password are provided
        if not email or not password:
            messages.error(request, "Both email and password are required.")
            return render(request, 'login.html')

        try:
            # Query the UserProfile (or User) model using email
            user = UserProfile.objects.get(email=email)  # Change to User.objects if using default User model
            print(user)
            print(user.password,user.email,user.phone_number)
            # Check if the provided password matches the stored hashed password
            if password==user.password:
                # If the password matches, log the user in
                auth_login(request, user)
                
                messages.success(request, "You have successfully logged in.")
                print("You have successfully logged in.")
                if user.type=='Partnership':
                    return redirect(partnership_view) 
                if user.type=='Candidate':
                    return redirect(candidate_view)  # Redirect to the homepage or dashboard
            else:
                messages.error(request, "Invalid email or password.")
                return render(request, 'login.html')

        except UserProfile.DoesNotExist:  # Or User.DoesNotExist if using the default User model
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')

    
def index(request):
    return render(request,"index.html")

def partnership_view(request):
    # Perform any necessary logic here (if needed)
    return render(request,'partnership.html')  # Redirect to the 'partnership' page

# View for redirecting to the candidate page
def candidate_view(request):
    # Perform any necessary logic here (if needed)
    return render(request,'candidate.html')  # Redirect to the 'candidate' page
