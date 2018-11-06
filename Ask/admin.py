from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(LikeDislike)
admin.site.register(Question)
admin.site.register(Answer)
