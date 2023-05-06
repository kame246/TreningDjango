from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'news/post/detail.html', {'post':post})

def post_list(request):
    cnt = Post.objects.count()
    posts = Post.objects.all()
    return render(request, 'news/post/list.html', {'imie':'Bartek', 'cnt':cnt,
                                                   'posts':posts})

    # return render(request, template_name='news/post/list.html',
    #               context={'imie':'Bartek'})

