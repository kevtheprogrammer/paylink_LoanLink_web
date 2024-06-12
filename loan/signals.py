from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Loan
from account.models import Notification

@receiver(post_save, sender=Loan)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # Create a notification for the newly created user
        Notification.objects.create(user_client=instance.customer.user, context="Dear customer! Your loan application has been received and is under moderation. You will receive a notification confirmation of your loan application")
