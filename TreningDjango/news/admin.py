from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    @staticmethod
    def created_year(obj):
        return obj.created.year

    @staticmethod
    def short_content(obj):
        return f'{obj.content[:10]}...'

    @admin.action(description='Clear content')
    @staticmethod
    def cleanup_content(model_admin, request, query_set):
        query_set.update(content='')

    @admin.action(description='Add Footer')
    @staticmethod
    def add_footer(model_admin, request, queryset):
        footer_text = '\n============ \n oto stopka'
        for post in queryset.exclude(content__endswith=footer_text):
            post.content += footer_text
            post.save()

    actions = ('cleanup_content', 'add_footer')
    list_display = ('title', 'author', 'category', 'created', 'created_year',
                    'short_content')
    search_fields = ('title', 'content')
    ordering = ('category', 'created')
    list_filter = ('author', 'category', 'created')
    date_hierarchy = 'created'
    raw_id_fields = ('author',)
    list_per_page = 5

# admin.site.register(Post)

