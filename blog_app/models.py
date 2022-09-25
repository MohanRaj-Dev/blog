from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
# Create your models here.


status = ((0, 'Draft'), (1, 'Publish'))
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    content = FroalaField()
    publish = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=status, default=0)

    class Meta:
        ordering = ['-publish']

    def __str__(self) -> str:
        return self.title