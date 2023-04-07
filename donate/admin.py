from django.contrib import admin
from .models import Donation, BulletinBoard, Expense, CrowdFunding

admin.site.register([Donation, BulletinBoard, Expense, CrowdFunding])
