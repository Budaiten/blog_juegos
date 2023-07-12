from django.shortcuts import render, redirect
from apps.posts.models import Categoria, Post
from .forms import SignupForm, LoginForm
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def index(request):
    posts = Post.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'index.html',{
        'categories': categoria,
        'posts': posts,
    })

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form':form
    })

def logout_view(request):
    logout(request)
    return redirect('index')