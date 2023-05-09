from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .forms import CommentForm

# class NewsDetail(View):
#     def get(self, request, *args, **kwargs):
#         # print(f'{args=} {kwargs=}')
#         id = kwargs['id']
#         post = get_object_or_404(Post, id=id)
#         return render(request, 'news/post/detail.html', {'post':post})

# class NewsDetail(TemplateView):
#     template_name = 'news/post/detail.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post'] = get_object_or_404(Post, id=kwargs['id'])
#         return context

def news_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False) # Nie chcę zapisać w bazie danych, bo ustawiam jeszcze post
        comment.post = post
        comment.save()
        return HttpResponseRedirect(request.path)
    return render(request, 'news/post/detail.html', {'post': post, 'form': form,
                                                     'comments': comments})

# class NewsDetail(DetailView):
#     template_name = 'news/post/detail.html'
#     model = Post

# class NewsList(View):
#     def get(self, request, *args, **kwargs):
#         posts_per_page = 3
#         cnt = Post.objects.count()
#         pg = Paginator(Post.objects.all(), posts_per_page)
#         page_num = request.GET.get('page')
#         try:
#             posts = pg.page(page_num)
#         except PageNotAnInteger:
#             posts = pg.page(1)
#         except EmptyPage:
#             posts = pg.page(pg.num_pages)
#         return render(request, 'news/post/list.html', {'imie':'Bartek', 'cnt':cnt,
#                                                        'posts':posts})

    # return render(request, template_name='news/post/list.html',
    #               context={'imie':'Bartek'})


# class NewsList(TemplateView):
#     template_name = 'news/post/list.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         posts_per_page = 3
#         context['cnt'] = Post.objects.count()
#         pg = Paginator(Post.objects.all(), posts_per_page)
#         page_num = self.request.GET.get('page')
#         try:
#             context['posts'] = pg.page(page_num)
#         except PageNotAnInteger:
#             context['posts'] = pg.page(1)
#         except EmptyPage:
#             context['posts'] = pg.page(pg.num_pages)
#
#         return context


class NewsList(ListView):
    template_name = 'news/post/list.html'
    extra_context = {'cnt':Post.objects.count(), 'imie':'Bartek'}
    paginate_by = 3 # Szablon używa zmiennej w URL o nazwie 'page', np. '?page=1'
    # W szablonie będzie obiekt paginacji pod nazwą 'page_obj'
    model = Post
    context_object_name = 'posts' # Bez tego lista postów byłaby przekazana do szablonu pod nazwą 'object_list'