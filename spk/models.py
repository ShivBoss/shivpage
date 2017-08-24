from django.db import models

# Create your models here.


class ImgBlog(models.Model):

	title = models.CharField(max_length=120)
	image = models.ImageField(null=True, blank=True, width_field="width_field", height_field='height_field')
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	context = models.TextField()
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


class MailMe(models.Model):

	email = models.EmailField()
	fullName = models.CharField(max_length=120)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)