from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password matches
        if password == password2:
            # Check for duplicate username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exist!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
                return redirect('register')
            else:
                # Register user
                user = User.objects.create_user(
                            username=username,
                            email=email,
                            password=password,
                            first_name=first_name,
                            last_name=last_name
                        )
                # Login after register
                '''auth.login(request, user=username)
                messages.success(request, 'Account created successfully')
                return redirect('index')'''
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    user_contact = Contact.objects.order_by('-id').filter(user_id=request.user.id)
    context = {
        'contacts': user_contact
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out!')
        return redirect('index')
