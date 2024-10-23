from django.contrib import admin
from .models import MyUser

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('date_joined',)

admin.site.register(MyUser, MyUserAdmin)
