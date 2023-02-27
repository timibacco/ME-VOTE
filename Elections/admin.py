from django.contrib import admin
from .models import ElectoralProcess
# Register your models here.
class ElectoralProcessAdmin(admin.ModelAdmin):
    
    list_display = ("name", "link", "no_of_voters","start_date", "end_date",)
    list_filter = ("start_date",)

admin.site.register(ElectoralProcess, ElectoralProcessAdmin)