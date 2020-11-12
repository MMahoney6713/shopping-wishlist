from django.contrib import admin
from .models import Group, AppUser, WishList

# Register your models here.
admin.site.register(Group)
admin.site.register(AppUser)
admin.site.register(WishList)
