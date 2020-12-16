from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime
from .models import Post
from django.template.defaultfilters import date
from taggit.models import Tag
from django.db.models import Count


def index(request, tag_slug=None):
    object_list = Post.posted.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': Post.posted.all(),
        'page': page,
        'tag': tag
    }

    return render(request, 'mainApp/index.html', context)


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='posted')

    context = {
        'post': post
    }

    return render(request, 'mainApp/post.html', context)
