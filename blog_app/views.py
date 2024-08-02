import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from blog_app.models import Post, UserProfile, Ice
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def posts(request):

    if request.method == 'POST':
        if 'username' in request.session:
            author = request.session['username']
        else:
            author = "방문자"

        post = Post.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            author=author
        )
        return redirect('posts')
        
    all_posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj
    }
    
    return render(request, 'posts.html', context)

def new_post(request):
    username = request.session.get('username', '방문자')
    context = {'username': username}
    return render(request, 'new_post.html', context)

def read_post(request, id: int):
    try:
        post = Post.objects.get(id=id)
        post.views += 1
        post.save()
    except Post.DoesNotExist:
        raise Http404('Post not found')
    
    context = {
            "post": post,
            "username": post.author,
            "views": post.views
        }
    return render(request, 'read_post.html', context)

def edit_post(request, id: int):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Post not found")
    
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("read_post", id)
    else:
        context = {
            "post": post,
            "username": post.author
        }
        return render(request, "edit_post.html", context)
    
def delete_post(request, id: int):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('posts')

# def changeNickname(request):
#     if request.method == 'POST':
#         new_nickname = request.POST.get('username')
#         if new_nickname:
#             request.session['username'] = new_nickname
#             return redirect('posts')
    
#     return render(request, 'changeNickname.html')

def join(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        
        user = User.objects.create_user(username=username, password=password)
        user_profile = UserProfile.objects.create(user=user, name=name)
        
        return redirect('posts')
    return render(request, 'join.html')

def board_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = user.userprofile.name
            return redirect('posts')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def board_logout(request):
    logout(request)
    return redirect('posts')

def review_list(request):
    images = Ice.objects.all()
    image_url_prefix = '/static/images/'
    return render(request, 'review_list.html', {'images': images, 'image_url_prefix': image_url_prefix})

def search_view(request):
    category = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '')

    if category == 'all':
        if search_query:
            images = Ice.objects.filter(name__icontains=search_query)
        else:
            images = Ice.objects.all()
    else:
        if search_query:
            images = Ice.objects.filter(category=category, name__icontains=search_query)
        else:
            images = Ice.objects.filter(category=category)

    image_url_prefix = "/static/images/"

    return render(request, 'review_list.html', {
        'images': images,
        'image_url_prefix': image_url_prefix,
        'selected_category': category,
        'search_query': search_query,
    })

# 확인용
def review_detail(request, name):
    item = get_object_or_404(Ice, name=name)
    return render(request, 'review_detail.html', {'item': item})