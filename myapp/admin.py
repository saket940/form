from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',
            'father_name',
            'address',
            'tenth_percentage',
            'contact_number',
            'passing_year',
            'current_school',
            'interested_branch',)