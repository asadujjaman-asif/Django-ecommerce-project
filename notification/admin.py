from django.contrib import admin

# Register your models here.
from notification.models import Notifications

admin.site.register(Notifications)