from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display    = ('judul', 'slug', 'status', 'created')
    list_filter     = ("status",)
    search_fields   = ['judul', 'postingan',]
    prepopulated    = {'slug':('judul')}
    readonly_fields = ['slug',]

# Register your models here.
admin.site.register(Post, PostAdmin)
