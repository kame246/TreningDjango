from django.db import models


class Preassure(models.Model):
    sys = models.PositiveSmallIntegerField()
    dia = models.PositiveSmallIntegerField()
    time = models.DateTimeField(auto_now_add=True)
