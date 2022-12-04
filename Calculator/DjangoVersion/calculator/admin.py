from django.contrib import admin

from .models import History

@admin.register(History)
class CustomHistoryAdmin(admin.ModelAdmin):
    pass 
