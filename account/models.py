from django.contrib.auth.models import User
from django.db import models
from django.contrib.humanize.templatetags import humanize

# Create your models here.

class Check(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,verbose_name="Владелец счета",
    )
    balance = models.FloatField("Баланс")
    created_at = models.DateField("Дата регистрации счета",auto_now_add=True)
    updated_at = models.DateField("Дата последних действий со счетом", auto_now=True)



class Transaction(models.Model):
    amount = models.FloatField("Сумма перевода")
    created_at = models.DateTimeField("Дата первода",auto_now_add=True)
    recipient = models.IntegerField("ID счета получателя")
    sender = models.ManyToManyField("Check", verbose_name="ID счетов получателя")