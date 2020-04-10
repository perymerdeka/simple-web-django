from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
STATUS = (
    (0, "Disimpan"),
    (1, "Publish"),
)

class Post(models.Model):
    judul       = models.CharField(max_length=255, unique=True)
    author      = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated     = models.DateTimeField(auto_now=True)
    postingan   = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    slug        = models.SlugField(max_length=255, unique=True, editable=False)
    status      = models.IntegerField(choices=STATUS, default=0)

    def save(self):
        self.slug = slugify(self.judul)
        super(Post, self).save()
    
    def __str__(self):
        return self.judul

    class Meta:
        ordering = ['-created']

     
