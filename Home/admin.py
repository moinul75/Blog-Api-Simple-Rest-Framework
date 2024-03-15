from django.contrib import admin
from .models import Category, Tag, Image, Blog, Reaction, Comment, Reply, BlogReadingTime, BlogWatchTime



admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Reaction)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Blog)
admin.site.register(BlogReadingTime)
admin.site.register(BlogWatchTime)


