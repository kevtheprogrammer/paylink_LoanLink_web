from __future__ import unicode_literals
from datetime import datetime
# import datetime
from django.utils import timezone
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.urls import reverse
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    TYPE_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    avatar = models.ImageField(
        upload_to='avatars/', null=True, blank=True, default='user.png')
    email = models.EmailField(verbose_name='email address', unique=True)
    email_confirmed = models.BooleanField(
        verbose_name='email confirmed', default=False)
    membership_id = models.CharField(max_length=900, blank=True)
    access_code = models.UUIDField(default=None, blank=True, null=True)
    first_name = models.CharField(
        verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(
        verbose_name='last name', max_length=30, blank=True)
    dob = models.DateField(auto_now=True, blank=True)
    nrc = models.CharField(
        verbose_name='national registration number', max_length=300, blank=True)
    nrc_front = models.ImageField(upload_to='identity/', null=True, blank=True)
    nrc_back = models.ImageField(upload_to='identity/', null=True, blank=True)
    country = CountryField(blank_label='(select country)', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    phone_home = models.CharField(max_length=20, blank=True)
    cover_plan = models.CharField(max_length=50, null=True, blank=True)
    phone_work = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    location = models.CharField(
        verbose_name='location', max_length=50, blank=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_verified = models.BooleanField(verbose_name='verified', default=False)
    creation_ip_address = models.CharField(
        max_length=24, default=None, blank=True, null=True)
    deletion_ip_address = models.CharField(
        max_length=24, default=None, blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Generate access_code if it's not set
        if not self.access_code:
            self.access_code = uuid.uuid4()
            # Get the current date in the format YYMMDD
            # current_date = datetime.now().strftime("%y%m%d")
            # # Generate the access_code using the specified pattern
            # self.access_code = f"OL{current_date}"

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-date_joined']

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        print(subject, message, from_email,)
        # send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        return reverse('account:profile', args=[self.pk])

    def get_verified_status(self):
        if self.is_verified:
            return "verified"
        return "not verified"

    def get_update_url(self):
        return reverse('account:profile-edit', args=[self.pk])

    def get_absolute_url(self):
        return reverse("account:user-details", kwargs={"pk": self.pk})

    def set_verify(self):
        return reverse("account:togle-verify", kwargs={"pk": self.pk})
