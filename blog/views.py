from django.shortcuts import render, redirect
from apps.posts.models import Categoria, Post
from .forms import SignupForm, LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def index(request):
    posts = Post.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'index.html',{
        'categories': categoria,
        'posts': posts,
    })

@login_required
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
    return redirect('/')


# Frontend general 
def frontGeneral(request):
    return render(request,'home.html')

# Frontend juegos
def juegos(request):
    return render(request,'juegos.html')

# Frontend Noticias
def noticias(request):
    return render(request,'noticias.html')


# Frontend perfil
@login_required
def perfil(request, id):
    return render(request, 'perfil.html')