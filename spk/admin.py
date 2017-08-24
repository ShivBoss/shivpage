from django.contrib import admin

# Register your models here.

from .models import ImgBlog
from .models import MailMe

class ImgBlogAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	class Meta:
		model = ImgBlog


class MailMeAdmin(admin.ModelAdmin):
	list_display = ["email", "fullName", "timestamp"]
	class Meta:
		model = MailMe


admin.site.register(ImgBlog, ImgBlogAdmin)

admin.site.register(MailMe, MailMeAdmin)