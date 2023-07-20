from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Post, Categoria
from .forms import NuevoPostForm, EditarPostForm

def items(request):
    query = request.GET.get('query','')
    categorias_id = request.GET.get('categorias_id', 0)
    categorias = Categoria.objects.all()
    posts = Post.objects.filter(is_sold=False)

    if categorias_id:
        posts = posts.filter(categoria_id=categorias_id)

    if query:
        posts = posts.filter(nombre__contains=query) | Q(texto__icontains=query)

    return render(request, 'posts.html',{
        'posts':posts,
        'query':query,
        'categorias': categorias,
    })


def detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts_relacionados = Post.objects.filter(categoria=post.categoria).exclude(pk=pk)
    return render(request, 'detalle.html', {
        'post':post,
        'posts_relacionados':posts_relacionados,
    })

@login_required
def nuevo(request):
    if request.method == 'POST':
        form = NuevoPostForm(request.POST, request.FILES)
        form.request = request  
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detalle', pk=post.id)
    else:
        form = NuevoPostForm()
        form.request = request  

    return render(request, 'form.html', {
        'form': form,
        'titulo': 'Nuevo Post',
    })


@login_required
def eliminar(request, pk):
    post = get_object_or_404(Post, pk=pk, autor=request.user)
    post.delete()

    return redirect('index')

@login_required
def editar(request, pk):
    post = get_object_or_404(Post, pk=pk, autor=request.user)

    if request.method == 'POST':
        form = EditarPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()

            return redirect('detalle',pk=post.id)
    else:
        form = EditarPostForm(instance=post)

    return render(request,'form.html', {
        'form':form,
        'titulo':'Editar Post',
    })