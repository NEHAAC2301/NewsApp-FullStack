
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
API_KEY = '371cd36dae2db9a650f241adea89b572'

def home(request):
    """
    Display some general details or top headlines on the home page.
    """
    url = f'https://gnews.io/api/v4/top-headlines?apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])  # Handle cases where 'articles' might be missing

    context = {
        'articles': articles[:5],  # Display only the top 5 articles on the home page
    }
    return render(request, 'news_api/home.html', context)

def search_news(request):
    """
    Handle user input and display news based on search criteria.
    """
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    
    
    articles = []
    if country:
        url = f'https://gnews.io/api/v4/search?q=example&country={country}&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data.get('articles', [])
    elif category:
        url = f'https://gnews.io/api/v4/top-headlines?category={category}&apikey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data.get('articles', [])

    context = {
        'articles': articles,
    }
    return render(request, 'news_api/search.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            next_url = request.GET.get('next', '/search/')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'news_api/login.html', {'form': form})

def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Your account has been created. Please log in.')
            return redirect('/login/')
    return render(request, 'news_api/signup.html')

