from django.contrib import admin

# Register your models here.
from account.models import Check, Transaction

admin.site.register(Check)
admin.site.register(Transaction)