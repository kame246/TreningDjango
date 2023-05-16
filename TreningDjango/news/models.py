from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    CATEGORIES = (
        ('IT', 'Informatyka'), # pierwsza wartość jest zapisana w bazie danych, a druga wyświetlana np. w formularzu
        ('G', 'Geografia'),
        ('Z', 'Zdrowie')
    )
    title = models.CharField(max_length=20)
    content = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #Ustawienie related_name powoduje, że User będzie posiadać listę postów pod nazwą 'posts', a nie standardowo 'post_set'
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.CharField(choices=CATEGORIES, max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            (
                "can_be_shared",
                "Post can be shared by clicking Share button"
            )
        ]

    def get_absolute_url(self):
        return reverse('news:detail', args=[self.id])

    def __str__(self):
        return f'Post: {self.title}'


class Comment(models.Model):
    nick = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    email = models.EmailField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Komentarz {{ self.content[:10] }}... dodany przez {self.nick} dla postu'