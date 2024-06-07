from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import UserLoginForm  # Replace with your login form import path
from collab.models import Login  # Import the Login model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UploadedFile


# View for the index page
def index(request):
    return render(request, 'index.html')


# View for the video call page
def videocall(request):
    return render(request, 'videocall.html')
def todo(request):
    return render(request, 'todo.html')
def sharing(request):
    return render(request, 'sharing.html')
def chatting(request):
    return render(request, 'chatting.html')


# View for handling user login
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('home')  # Replace 'home' with your desired URL name
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Form is not valid.")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def save_login_data(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Cleaned data from form
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # Create a new Login instance
            login_instance = Login(
                username=name,
                email=email,
            )
            login_instance.save()
            
            messages.success(request, "Account has been created successfully.")
            
            # Redirect to the sign-in form page after successful form submission
            return redirect('signup')  # Replace 'sign_in' with the URL name of the sign-in page
        else:
            messages.error(request, "Form is not valid. Please check the input fields.")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        filename = uploaded_file.name

        # Save the file to the database
        file_instance = UploadedFile(file=uploaded_file, filename=filename)
        file_instance.save()

        # Generate download link
        download_link = request.build_absolute_uri(file_instance.file.url)

        # Return the download link in JSON response
        return JsonResponse({
            'status': 'success',
            'download_link': download_link,
            'filename': filename
        })

    return JsonResponse({'status': 'error', 'message': 'No file uploaded'})