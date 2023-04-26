from django.shortcuts import render
from .models import Post

def post_list(request):
    cnt = Post.objects.count()
    posts = Post.objects.all()
    return render(request, 'news/post/list.html', {'imie':'Bartek', 'cnt':cnt,
                                                   'posts':posts})

    # return render(request, template_name='news/post/list.html',
    #               context={'imie':'Bartek'})
