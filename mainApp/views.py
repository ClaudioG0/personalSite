from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):


    context = {

    }

    return render(request, 'mainApp/index.html')


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='posted', publish__year=year,
                             publish_month=month, publish__day=day)

    context = {
        'post': post
    }

    return render(request, 'post.html', context)
