<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html',{'blog':blog})
=======
from django.shortcuts import render
from .models import Blog
# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
>>>>>>> 3bdcdc1034400883ca1aba4725c23e0524c55afc
