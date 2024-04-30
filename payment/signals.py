from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import LoanTransaction
from account.models import Notification
from django.core.exceptions import ValidationError


@receiver(pre_save, sender=LoanTransaction)
def check_loan_repayment_balance(sender, instance, **kwargs):
    if instance.transaction_type == 'Loan Repayment':
        if instance.client.balance == 0:
            # Create a notification for the client
            msg = "Cannot Pay loan, your outstanding loan balance is K0.00. Thank you for trusting us!"
            Notification.objects.create(user_client=instance.client.user, context=msg)
            # Raise a validation error to prevent saving the transaction
            raise ValidationError(msg)
        elif instance.amount > instance.client.balance:
            # Create a notification for the client
            msg = "Loan Repayment amount cannot exceed client's outstanding loan balance."
            Notification.objects.create(user_client=instance.client.user, context=msg)
            # Raise a validation error to prevent saving the transaction
            raise ValidationError(msg)
        
@receiver(post_save, sender=LoanTransaction)
def create_notification(sender, instance, created, **kwargs):
    try:
        if created:
            msg = 'loan transaction created'
            # Create a notification for the newly created user
            if instance.transaction_type == 'Disbursement':
                # disburse funds to user account add to balance
                instance.client.balance += float(instance.loan_obj.payable_amount)
                instance.client.save()
                msg = f'Dear customer! Your {instance.loan_obj.payable_amount} loan has been disbursed in your account with a monthly payable of ZMK{instance.loan_obj.get_monthly_payable} for {instance.loan_obj.period} months. Thank you for trusting us.'
                instance.loan_obj.status = 'active'
                instance.loan_obj.save()

            elif instance.transaction_type == 'Loan Repayment':
                # remove from balance
                instance.client.balance -= float(instance.amount)
                instance.client.save()
                if float(instance.client.balance) == 0.0:
                    msg = f'You have paid {instance.amount} towards your {instance.loan_obj.payable_amount}. Thank you for clearing your loan. Good things are coming.'
                    # change loan status 
                    instance.loan_obj.status = 'closed'
                    instance.loan_obj.save()
                else:
                    msg = f'You have paid {instance.amount} towards your {instance.loan_obj.payable_amount}. Your outstanding loan balance is {instance.client.balance}. Thank you for trusting us.'

            elif instance.transaction_type == 'Penalty':
                # add to balance 
                instance.client.balance += float(instance.amount)
                instance.client.save()
                msg = f'Dear customer! You have incurred a penalty fee of {instance.amount} towards your {instance.loan_obj.payable_amount}. Please pay your loan on time. Your outstanding loan balance is {instance.client.balance}. Thank you for trusting us.'
            
            elif instance.transaction_type == 'Bad Debt':
                # add to balance 
                instance.client.balance += float(instance.amount)
                instance.client.save()  
                msg = f'Dear customer! You have incurred a bad debt fee of {instance.amount} towards your {instance.loan_obj.payable_amount}. Your outstanding loan balance is {instance.client.balance}. Thank you for trusting us.'
                                 
            Notification.objects.create(user_client=instance.client.user, context=msg)
    except Exception as e:
        # Handle the exception
        print(f"An error occurred: {e}")
