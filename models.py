from django.db import models
from django.core.validators import RegexValidator

class Appointment(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
    )
    message = models.TextField()
    preferred_date = models.DateField()
    preferred_time = models.TimeField()  # Updated from CharField to TimeField
    appointment_type = models.CharField(
        max_length=50,
        choices=[
            ("consultation", "Consultations"),
            ("nutrition-counseling", "Nutrition Counseling"),
        ],
    )
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('preferred_date', 'preferred_time')

    def __str__(self):
        return f"{self.full_name} - {self.preferred_date} {self.preferred_time}"

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"