from django.contrib import admin

# Register your models here.

from Users.models import users
admin.site.register(users)
