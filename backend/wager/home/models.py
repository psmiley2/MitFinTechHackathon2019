from django.db import models
from datetime import datetime
from django.conf import settings
import datetime

class Questions(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    education_lvl = models.IntegerField()
    annual_income = models.IntegerField()
    net_worth = models.IntegerField()
    known_expenses = models.IntegerField()
    possible_expenses = models.IntegerField()
    liquidity_needs = models.IntegerField()
    investment_objectives = models.IntegerField() 
    risk_tolerance = models.IntegerField()
    last_reviewed = models.DateField(auto_now_add=True, blank=True)
    reviewed_notes = models.TextField()
    beta = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, default=0.0)
    investment_experience = models.IntegerField(default=0)
    at_risk = models.IntegerField(default=0)

    def __str__(self):
        return self.name
