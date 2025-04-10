from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from questions.models import Question

def home(request):
    """
    View to show all questions
    """
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'user/home.html', {'questions': questions})

def signup(request):
    """
    View to handle signup for user
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

def login_user(request):
    """
    View to handle authenticate user
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def logout_user(request):
    """
    View to logout user
    """
    logout(request)
    return redirect('login')
