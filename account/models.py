import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .managers import *
from django.contrib.auth.models import PermissionsMixin
	


class User(AbstractBaseUser, PermissionsMixin):
    
    USER_TYPE = (
 
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
        ('Customer', 'Customer'),
        ('Agent', 'Agent'),
    )
    
    ID_TYPE = (
        ('NRC', 'NRC'),
        ('Passport', 'Passport'),
        ('Lisense', 'Lisense'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )


    # MARTIAL_STATUS = (
    #     ('Married', 'Married'),
    #     ('Single', 'Single'),
    #     ('Divorced', 'Divorced'),
    #     ('Widowed', 'Widowed'),
    #     ('Widow', 'Widow'),
    # )

 

    RELATION = (
        ('Son', 'Son'),
        ('Daughter', 'Daughter'),
        ('Husband', 'Husband'),
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
    )

    FAMILY_TYPE = (
        ('Extended', 'Extended'),
        ('Nuclear', 'Nuclear'),
    )

    ID_TYPE = (
        ('NRC', 'NRC'),
        ('Passport', 'Passport'),
        ('Lisense', 'Lisense'),
    )

    user_type = models.CharField(max_length=50, verbose_name='User Role', choices=USER_TYPE, default='Customer')
    profile_pic = models.ImageField(upload_to='avatars/', blank=True)
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    # middle_name = models.CharField(max_length=50, verbose_name='Middle Name', blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField('Date of Birth', null=True, blank=True)
    id_type = models.CharField(max_length=50, choices=ID_TYPE)
    id_number = models.CharField(verbose_name='identtity number', max_length=300, blank=True)
    location = models.CharField(verbose_name='location', max_length=50, blank=True)

    id_front = models.ImageField(upload_to='id_front/', null=True, blank=True)
    id_back = models.ImageField(upload_to='id_back/', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='Male')
    # marital_status = models.CharField(max_length=9, verbose_name='Marital status', choices=MARTIAL_STATUS, default='Single', blank=True)
    city = models.CharField(max_length=100, blank=True)
    # family_type = models.CharField(max_length=20, choices=FAMILY_TYPE, blank=True, default=None)
    address = models.CharField(max_length=200)

    is_staff = models.BooleanField(verbose_name='staff', default=False)
    is_supervisor = models.BooleanField(verbose_name='staff', default=False)
    is_manager = models.BooleanField(verbose_name='staff', default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_crm = models.BooleanField(verbose_name='crm manager', default=False)
    is_verified = models.BooleanField(verbose_name='verified', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class ClientProfile(models.Model):
 
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    empolyee_number = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    bank = models.CharField(max_length=200, blank=True, null=True)
    bank_acc = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
           return f'{self.email}'

    class Meta:
	
	    db_table = "client_profile"



class AgentProfile(models.Model):
      GENDER =(
          ('Male', 'Male'),
          ('Female', 'Female'),
      )
    #   agent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      client = models.ForeignKey(User, on_delete=models.CASCADE)
      bank = models.CharField(max_length=200, blank=True, null=True)
      bank_acc = models.CharField(max_length=200, blank=True, null=True)
      date_joined = models.DateField(auto_now_add=True)
      is_active = models.BooleanField(default=True)
      is_agent = models.BooleanField(default=True)
      is_staff = models.BooleanField(default=False)

      class Meta:
	      db_table = "agent_profile"

