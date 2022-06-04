from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Blog(models.Model):
    name = models.CharField(
        max_length=255555,
        db_index=True,
        blank=True,
        verbose_name='name'
    )
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        blank=True,
        verbose_name='Фотки'
    )
    text = models.CharField(
        max_length=255555,
        db_index=True,
        blank=True,
        verbose_name='text'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
