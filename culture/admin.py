from django.contrib import admin
from .models import CulturalPost

@admin.register(CulturalPost)
class CulturalPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
