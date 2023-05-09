from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nick', 'email', 'content')
        # exclude = ('created') # Wszystkie pola z wyjątkiem 'created' - alternatywne podejście zamiast fields =