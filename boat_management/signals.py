# boat_management/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Boat
from user_authentication.models import Authority

@receiver(post_save, sender=Boat)
def notify_authorities(sender, instance, created, **kwargs):
    if created and (instance.lifejacket < instance.capacity or instance.fire_extinguisher < 1):
        authorities = Authority.objects.all()

        if authorities:
            subject = 'Boat Notification'
            message = (
                f"A new boat '{instance.name}' (Registration No: {instance.reg_no}) "
                f"has been added with insufficient safety equipment."
            )
            from_email = 'roshnialdrin@gmail.com'  # Update this with your email
            recipient_list = [authority.user.email for authority in authorities]

            send_mail(subject, message, from_email, recipient_list)
            
