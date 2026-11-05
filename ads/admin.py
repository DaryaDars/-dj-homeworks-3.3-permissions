from django.contrib import admin
from ads.models import Ad

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'creator', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')