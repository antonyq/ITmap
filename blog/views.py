from django.shortcuts import get_object_or_404, render
from django.conf import settings
from math import ceil, floor
from blog.models import Post


def blog(request, current_page=1):
    current_page = int(current_page)
    posts = Post.objects.all()
    all_pages_count = ceil(posts.count() / settings.POSTS_PER_PAGE) 
    
    tail = int((settings.BULLETS_IN_PAGINATION - 1) / 2)
    a = max(0, tail - current_page + 1)
    b = max(0, current_page - (all_pages_count - tail))
    first_page_number = current_page - (tail + b - a)
    last_page_number = current_page + (tail - b + a) 
        
    first_post_number = max(0, posts.count() - current_page * settings.POSTS_PER_PAGE)
    last_post_number = posts.count() - (current_page - 1) * settings.POSTS_PER_PAGE 

    return render(request, 'blog.html', {
        'all_pages_count': all_pages_count,
        'pages': [i for i in range(first_page_number, last_page_number + 1)],
        'previous_page': current_page - 1,
        'next_page': current_page + 1,
        'current_page': current_page,
        'posts': posts[first_post_number:last_post_number:-1]
    })

def post(request, id=1):
    post = Post.objects.get(id = id)
    return render(request, 'post.html', {
        'post': post
    })