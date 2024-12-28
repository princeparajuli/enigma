# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    return render(request, 'home.html')

# House plan page
def houseplan(request):
    return render(request, 'houseplan.html')

# Registration page view
def registerpg(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user data
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('loginpg')
    else:
        form = RegisterForm()
    return render(request, "registerpg.html", {'form': form})

# Login page view

def loginpg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Pass both the request and the user
            return redirect('home')  # Redirect to a success page
        else:
            return render(request, 'loginpg.html', {'error': 'Invalid credentials'})
    return render(request, 'loginpg.html')



@login_required
def generation(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        width = request.POST.get('width')
        budget = request.POST.get('budget')
        noRooms = request.POST.get('noRooms')
        # Add logic to generate house plan based on these inputs
        context = {
            'length': length,
            'width': width,
            'budget': budget,
            'noRooms': noRooms,
        }
        return render(request, 'generation.html', context)
    else:
        return redirect('home')  # Redirect to home if accessed directly
