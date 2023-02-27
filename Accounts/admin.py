from django.contrib import admin
from .models import Participant
# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("email","first_name","last_name","password","is_voter","is_official","is_super_official")
    list_filter = ("email","electoral_process","groups", "is_voter","is_official", "is_super_official") 
admin.site.register(Participant, ParticipantAdmin)
