from django.shortcuts import render
from .documents import PostDocument


def search_view(request):

    q = request.GET.get('q')

    if q:
        posts = PostDocument.search().query('match', title=q)
    else:
        posts = ""

    context = {
        'posts': posts
    }
    return render(request, 'search/search.html', context)
