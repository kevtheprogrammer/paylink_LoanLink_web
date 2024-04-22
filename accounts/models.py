from __future__ import unicode_literals
# import datetime
from django.utils import timezone
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.urls import reverse
from django_countries.fields import CountryField

from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    
    USER_TYPE = (
 
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('Customer', 'Customer'),
        ('Agent', 'Agent'),
        ('Employee', 'Employee'),
    )
    
    ID_TYPE = (
        ('NRC', 'NRC'),
        ('Passport', 'Passport'),
        ('Lisense', 'Lisense'),
    )
    
    profile_pic = models.ImageField(upload_to='avatars/', null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE)
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    dob = models.DateField('Date of Birth', null=True, blank=True)
    id_type = models.CharField(max_length=50, choices=ID_TYPE)
    id_number = models.CharField(verbose_name='identtity number', max_length=300, blank=True)
    country = CountryField(blank_label='(select country)', blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(verbose_name='location', max_length=50, blank=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    is_supervisor = models.BooleanField(verbose_name='staff', default=False)
    is_manager = models.BooleanField(verbose_name='staff', default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_crm = models.BooleanField(verbose_name='crm manager', default=False)
    is_verified = models.BooleanField(verbose_name='verified', default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

 
    def __str__(self):
        
        return f'{self.first_name} {self.last_name}'
 
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = f'{self.first_name} {self.last_name}'
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
 
    def get_user_type(self):
        if self.user_type == 'admin':
            return 'Admin'
        elif self.user_type =='staff':
            return 'Staff'
        elif self.user_type == 'customer':
            return 'Customer'
        elif self.user_type == 'agent':
            return 'Agent'
        elif self.user_type == 'employee':
            return 'Employee'
        else:
            return self.user_type

