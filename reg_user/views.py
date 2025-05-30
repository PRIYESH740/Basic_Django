import requests
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .serializers import *
from django.contrib import messages
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def some_data_view(request):
    user = request.user
    data = {
        "message": f"Welcome, {user.username}!",
        "user": {
            "username": user.username,
            "email": user.email,
            "is_staff": user.is_staff,
            "date_joined": user.date_joined,
        }
    }
    return Response(data)


def logout_view(request):
    request.session.flush()  # Clear all session data
    return redirect('login')  


def register_view(request):
    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'password2': request.POST.get('password2')
        }

        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            account = serializer.save()
            refresh = RefreshToken.for_user(account)
            request.session['access'] = str(refresh.access_token)
            request.session['refresh'] = str(refresh)
            return redirect('dashboard')
        
        # Return with errors in context
        return render(request, 'login.html', {'errors': serializer.errors})

    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        response = requests.post('http://localhost:8000/account/login/', data={
            'username': username,
            'password': password
        })

        if response.status_code == 200:
            tokens = response.json()
            request.session['access'] = tokens['access']
            request.session['refresh'] = tokens['refresh']
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'login_error': 'Invalid credentials'})

    return render(request, 'login.html')

def convert_sets(obj):
    if isinstance(obj, dict):
        return {k: convert_sets(v) for k, v in obj.items()}
    elif isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, list):
        return [convert_sets(i) for i in obj]
    else:
        return obj

def dashboard_view(request):
    access = request.session.get('access')
    if not access:
        return redirect('login')  # Redirect to login if no token

    headers = {'Authorization': f'Bearer {access}'}
    response = requests.get('http://localhost:8000/account/api/some-data/', headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        data = {"error": "Failed to fetch data from API"}

    # Convert any sets inside data to lists
    data = convert_sets(data)

    data_json = json.dumps(data, indent=4)

    return render(request, 'dashboard.html', {'data': data_json})
   

