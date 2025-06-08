from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from login.models import CustomUser  # Import your custom user model

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CustomAuthenticationForm(request.POST or None)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Create user but don't save yet
            user = form.save(commit=False)
            
            # Normalize email to lowercase
            user.email = form.cleaned_data['email'].lower()
            
            # Set the username (can be non-unique)
            user.username = form.cleaned_data['username']
            
            # Now save with the custom fields
            user.save()
            
            # Log the user in after registration
            login(request, user)
            messages.success(request, f'Welcome {user.username}! Registration successful!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'login_register.html', {
        'form': form,
        'form_type': 'register'  # Pass form type to template
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = CustomAuthenticationForm(request.POST or None)

    if request.method == 'POST':
        # Use email for authentication
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        # Authenticate using email
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username or user.email.split("@")[0]}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login_register.html', {
        'form': form,
        'form_type': 'login'  # Pass form type to template
    })

@login_required
def logout_view(request):
    username = request.user.username or request.user.email.split("@")[0]
    logout(request)
    messages.info(request, f'Goodbye, {username}! You have been logged out.')
    return redirect('login')

@login_required
def home_view(request):
    user = request.user
    display_name = user.username or user.email.split("@")[0]
    return render(request, 'index.html', {
        'display_name': display_name
    })