from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.
class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone=models.CharField(blank=True,max_length=20)
	address = models.CharField(blank=True,max_length=200)
	city = models.CharField(blank=True,max_length=200)
	country = models.CharField(blank=True,max_length=200)
	image=models.ImageField(blank=True,upload_to='user_img')



def __str__(self):
		return self.user.username

def user_name(self):
	return self.user.first_name + ' ' + self.user.last_name + '[' + self.user.username + ']'

def image_tags(self):
	return mark_safe('<img src="{}" height="70"width="60"/>'.format(self.image.url))
image_tags.short_description = 'Image'


def imageUrl(self):
	if self.image:
		return self.image.url
	else:
		return ""