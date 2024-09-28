from django.db import models
from django.contrib import admin

class Bankloan(models.Model):
    Loanid = models.IntegerField(primary_key=True)
    CreditRate = models.IntegerField()
    Age = models.IntegerField()  
    Account_No = models.IntegerField()
    Reason = models.CharField(max_length=500)

class BankloanAdmin(admin.ModelAdmin):
    list_display = ('Loanid', 'CreditRate', 'Age', 'Account_No', 'Reason')