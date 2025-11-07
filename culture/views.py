from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from .models import CulturalPost

def home(request):
    posts = CulturalPost.objects.all().order_by('-created_at')
    return render(request, 'culture/home.html', {'posts': posts})

def heritage_sites(request):
    posts = CulturalPost.objects.filter(category='heritage')
    return render(request, 'culture/heritage.html', {'posts': posts})

def festivals(request):
    posts = CulturalPost.objects.filter(category='festival')
    return render(request, 'culture/festivals.html', {'posts': posts})

def artforms(request):
    posts = CulturalPost.objects.filter(category='artform')
    return render(request, 'culture/artforms.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(CulturalPost, id=id)
    return render(request, 'culture/post_detail.html', {'post': post})

@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        CulturalPost.objects.create(
            title=title,
            description=desc,
            category=category,
            image=image
        )
        messages.success(request, "Post added successfully!")
        return redirect('home')

    return render(request, 'culture/add_post.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

@login_required
def delete_post(request, id):
    post = get_object_or_404(CulturalPost, id=id)
    post.delete()
    messages.success(request, f"Post '{post.title}' has been deleted successfully!")
    return redirect('home')