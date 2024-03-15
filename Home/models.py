from django.db import models
from django.utils.text import slugify
from ipware import get_client_ip
import uuid 
from Account.models import CustomUser

class BlogBase(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  
        

class Tag(BlogBase):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Category(BlogBase): 
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Image(models.Model):
    image = models.ImageField(upload_to='Blog')

class Blog(BlogBase):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True,default='')
    blog_text = models.TextField()
    main_image = models.ImageField(upload_to='Blog', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')
    images = models.ManyToManyField(Image, related_name='blogs', blank=True)
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def count_reactions(self):
        return self.reactions.count() if hasattr(self, 'reactions') else 0 
    def count_replies(self):
        return self.replies.count() if hasattr(self, 'replies') else 0
    
    def __str__(self) -> str:
        return self.title

class Reaction(BlogBase):
    LIKE = 'like'
    LOVE = 'love' 
    HAHA = 'haha'
    ANGRY = 'angry'

    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (LOVE, 'Love'),
        (HAHA, 'Haha'),
        (ANGRY, 'Angry'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reactions')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='reactions')
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

class Comment(BlogBase):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    reactions = models.ManyToManyField(Reaction, related_name='comment_reactions', blank=True)

class Reply(BlogBase):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='replies')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    reply_text = models.TextField()
    reactions = models.ManyToManyField(Reaction, related_name='reply_reactions', blank=True) 




class BlogReadingTime(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='reading_times')
    ip_address = models.CharField(max_length=45)  # IPv6 can have 45 characters
    reading_time_seconds = models.PositiveIntegerField(default=0)

    @classmethod
    def update_or_create_reading_time(cls, blog, request):
        ip, _ = get_client_ip(request)
        if ip:
            reading_time_obj, created = cls.objects.get_or_create(blog=blog, ip_address=ip)
            if not created:
                # Update existing reading time
                reading_time_obj.reading_time_seconds += 1  # Increase reading time by 1 second
                reading_time_obj.save()

class BlogWatchTime(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='watch_times')
    ip_address = models.CharField(max_length=45)  # IPv6 can have 45 characters
    watch_time_seconds = models.PositiveIntegerField(default=0)

    @classmethod
    def update_or_create_watch_time(cls, blog, request):
        ip, _ = get_client_ip(request)
        if ip:
            watch_time_obj, created = cls.objects.get_or_create(blog=blog, ip_address=ip)
            if not created:
                # Update existing watch time
                watch_time_obj.watch_time_seconds += 1  # Increase watch time by 1 second
                watch_time_obj.save()
 