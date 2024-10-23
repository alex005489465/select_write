"""
from django.contrib import admin
from .models import SalesForm_Data

admin.site.register(SalesForm_Data)
"""

from django.contrib import admin
from .models import SalesForm_Data

class SalesForm_DataAdmin(admin.ModelAdmin):
    list_display = ('sales_form_id', 'productName', 'created_at', 'user')  # 顯示 productName, created_at, 和 user
    list_filter = ('user',)
    search_fields = ('productName', 'user__username')
                     
admin.site.register(SalesForm_Data, SalesForm_DataAdmin)
