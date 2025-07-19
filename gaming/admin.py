from django.contrib import admin
from .models import Séance

@admin.register(Séance)
class SéanceAdmin(admin.ModelAdmin):
    list_display = ('code', 'titre', 'date_début', 'etat')
    search_fields = ('titre', 'code')
    list_filter = ('etat',)
    
    actions = ['reset_state']
    
    def reset_state(self, request, queryset):
        queryset.update(etat='dispo')
    reset_state.short_description = "Reset state to 'dispo'"