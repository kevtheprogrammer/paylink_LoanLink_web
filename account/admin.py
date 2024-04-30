from django.contrib import admin
from .models import User, Notification

admin.site.register([User,Notification])