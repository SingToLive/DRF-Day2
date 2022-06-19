from django.contrib import admin
from .models import CustomUser as CustomUserModel
# Register your models here.
admin.site.register(CustomUserModel)
