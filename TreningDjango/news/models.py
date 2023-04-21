from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    CATEGORIES = (
        ('IT', 'Informatyka'), # pierwsza wartość jest zapisana w bazie danych, a druga wyświetlana np. w formularzu
        ('G', 'Geografia'),
        ('Z', 'Zdrowie')
    )
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORIES, max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post: {self.title}'