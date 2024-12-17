from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment  # Make sure this import isn't placed at the top globally
from django.core.mail import send_mail

@receiver(post_save, sender=Appointment)
def send_confirmation_email(sender, instance, created, **kwargs):
    # Check if the appointment is confirmed and it's not a new instance
    if not created and instance.is_confirmed:
        # Send confirmation email
        send_mail(
            'Appointment Confirmed',
            f"Dear {instance.full_name},\n\nYour appointment has been confirmed for {instance.preferred_date} at {instance.preferred_time}.\n\nThank you!",
            'no-reply@yourdomain.com',
            [instance.email],
            fail_silently=False,
        )
