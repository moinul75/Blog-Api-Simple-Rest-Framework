from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
RELEATIONSHIP_STATUS = [
    ('sigle', 'Single'),
    ('married', 'Married'),
]


# Role-based user model 
class CustomUser(AbstractUser):
    # Define role choices
    ROLE_CHOICES = [
        ('author', 'Author'),
        ('moderator', 'Moderator'),
        ('superadmin', 'Superadmin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# User profile model
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='cover_photos', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    relationship_status = models.CharField(max_length=20, choices=RELEATIONSHIP_STATUS, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    interested_in = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

