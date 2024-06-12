from django.contrib import admin
from .models import User, Notification,ClientProfile

admin.site.register([User,Notification, ClientProfile])