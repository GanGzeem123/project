from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import userlist
from django.db.models import Q
import re

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Debugging statement
        print(f"Attempting to log in with username: {username}")

        if len(username) > 1:
            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Debugging statement
                print(f"Authentication successful for user: {username}")

                # Log the user in
                django_login(request, user)
                return redirect('feed')  # Redirect to the feed page upon successful login
            else:
                # Debugging statement
                print(f"Authentication failed for user: {username}")

                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            # Invalid username length
            messages.error(request, 'Invalid username. Please enter a valid username.')

    return render(request, 'login.html')

def is_valid_email(email):
    return re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email)

def is_valid_username(username):
    return re.match(r'^[a-zA-Z0-9]+$', username)

def is_valid_password(password):
    return any(char.isalpha() for char in password) and any(char.isdigit() for char in password)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']

        # Additional validation
        if not is_valid_email(email):
            messages.error(request, 'Invalid email format. Please use a valid Gmail address.')
        elif not is_valid_username(username):
            messages.error(request, 'Invalid username. Please use only letters and numbers.')
        elif not is_valid_password(password):
            messages.error(request, 'Invalid password. Please use a combination of letters and numbers.')
        elif password == cpassword:
            # Check if the username or email already exists
            if userlist.objects.filter(username__iexact=username).exists() or userlist.objects.filter(useremail__iexact=email).exists():                messages.error(request, 'Username or email already exists.')
            else:
                # Create a new user and save to the database
                new_user = userlist(username=username, useremail=email)
                new_user.set_password(password)
                new_user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')

def reset(request):
    return render(request, 'reset.html')

def resetpass(request):
    return render(request, 'resetpass.html')

def bar(request):
    return render(request, 'bar.html')

def profile(request):
    return render(request, 'profile.html')

@login_required
def feed(request):
    # Debugging statement
    print(f"User {request.user.username} is accessing the feed page.")
    return render(request, 'feed.html')

def chat(request):
    return render(request, 'chat.html')


def friends(request):
    searched_users = userlist.objects.all()
    search_query = request.GET.get('search_query', '').lower()

    if search_query and search_query not in ['#all', '#ALL']:
        searched_users = userlist.objects.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(nickname__icontains=search_query) |
            Q(gender__iexact=search_query) |  # Use 'iexact' for case-insensitive comparison
            Q(age__icontains=search_query)
        )
    elif search_query in ['#all', '#ALL']:
        searched_users = userlist.objects.all()

    return render(request, 'friends.html', {'searched_users': searched_users})
