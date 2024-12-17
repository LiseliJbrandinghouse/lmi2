from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from .forms import AppointmentForm
from .models import Appointment
from .forms import ContactForm




def home(request):
    return render(request, 'index.html')
# Create your views here.

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            contact_submission = form.save()

            # Send email to admin
            send_mail(
                subject=f"New Contact Submission from {contact_submission.name}",
                message=f"Name: {contact_submission.name}\nEmail: {contact_submission.email}\n\nMessage:\n{contact_submission.message}",
                from_email='no-reply@yourdomain.com',
                recipient_list=['mukelabai49@gmail.com'],  # Replace with admin's email
                fail_silently=False,
            )

            # Add success message
            messages.success(request, "Thank you for contacting us! We will get back to you soon.")
            return render(request, 'contact.html', {'form': ContactForm()})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            # Notify admin
            send_mail(
                'New Appointment Request',
                f"An appointment request has been made:\n\n{appointment}",
                'no-reply@yourdomain.com',
                ['mukelabai49@gmail.com'],
                fail_silently=False,
            )
            messages.success(
                request,
                'Your appointment has been successfully submitted! We will contact you soon.'
            )
    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {'form': form})

def confirm_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.is_confirmed = True
    appointment.save()

    # Notify user
    send_mail(
        'Appointment Confirmed',
        f"Dear {appointment.full_name},\n\nYour appointment has been confirmed for {appointment.preferred_date} at {appointment.preferred_time}.",
        'no-reply@yourdomain.com',
        [appointment.email],
        fail_silently=False,
    )
    return redirect('admin_appointment_list')  # Redirect to admin list view

def unavailable_slots(request):
    appointments = Appointment.objects.filter(is_confirmed=True)
    unavailable = [
        {'date': a.preferred_date, 'time': a.preferred_time}
        for a in appointments
    ]
    return JsonResponse({'unavailable': unavailable})
