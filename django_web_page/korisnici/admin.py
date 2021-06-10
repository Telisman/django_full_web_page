from django.contrib import admin
from .models import CustomKorisnici,TaskCategory,Post,Comment

admin.site.register(CustomKorisnici)
admin.site.register(TaskCategory)
admin.site.register(Post)
admin.site.register(Comment)
