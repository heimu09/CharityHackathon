from django.contrib import admin
from .models import Donation, BulletinBoard

admin.site.register([Donation, BulletinBoard])
