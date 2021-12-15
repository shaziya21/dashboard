from django.contrib import admin
from .models import Post,Signup,homescreen,suggestions
# Register your models here.

admin.site.register(Post)
admin.site.register(Signup)
admin.site.register(homescreen)
admin.site.register(suggestions)

