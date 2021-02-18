from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    GROUP = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('B-', 'B-'),
        ('O+', 'O-'),
    ]
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=256, null=True, blank=True)
    blood_group = models.CharField(max_length=10, choices=GROUP, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    Location = models.CharField(max_length=256, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True,)
    contact_no = models.CharField(max_length=256, null=True, blank=True)
    availability = models.BooleanField(default=True)
    img = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.img.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.img.path)
