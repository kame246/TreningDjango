from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View

class NewsDetail(View):
    def get(self, request, *args, **kwargs):
        # print(f'{args=} {kwargs=}')
        id = kwargs['id']
        post = get_object_or_404(Post, id=id)
        return render(request, 'news/post/detail.html', {'post':post})

class NewsList(View):
    def get(self, request, *args, **kwargs):
        posts_per_page = 3
        cnt = Post.objects.count()
        pg = Paginator(Post.objects.all(), posts_per_page)
        page_num = request.GET.get('page')
        try:
            posts = pg.page(page_num)
        except PageNotAnInteger:
            posts = pg.page(1)
        except EmptyPage:
            posts = pg.page(pg.num_pages)
        return render(request, 'news/post/list.html', {'imie':'Bartek', 'cnt':cnt,
                                                       'posts':posts})

    # return render(request, template_name='news/post/list.html',
    #               context={'imie':'Bartek'})

