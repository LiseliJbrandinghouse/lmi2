from django.contrib import admin
from .models import Appointment
from .models import ContactSubmission

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'preferred_date', 'preferred_time', 'is_confirmed')
    list_filter = ('preferred_date', 'is_confirmed')

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # Display these fields in the list view
    search_fields = ('name', 'email', 'message')  # Enable search by name, email, or message
    list_filter = ('submitted_at',)  # Add a filter by submission date
    readonly_fields = ('name', 'email', 'message', 'submitted_at')  # Make fields read-only

admin.site.register(ContactSubmission, ContactSubmissionAdmin)