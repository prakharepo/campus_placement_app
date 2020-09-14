from django.contrib import admin
from .models import company, Post, application
# Register your models here.
admin.site.register(company)
admin.site.register(Post)
admin.site.register(application)