from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Notification,ClientProfile

@receiver(post_save, sender=User)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # Create a notification for the newly created user
        Notification.objects.create(user_client=instance, context="Welcome to our platform, please complete your KYC and verification to access our products and servces. Good things are coming!")


@receiver(post_save, sender=User)
def create_client_profile(sender, instance, created, **kwargs):
    if created:
        # Create a notification for the newly created user
        ClientProfile.objects.create(user=instance, empolyee_number=instance.id)
