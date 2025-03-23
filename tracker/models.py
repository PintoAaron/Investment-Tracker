from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




class Investment(models.Model):
    
    PERIOD_CHOICES = [
        ('Yearly', 'Yearly'),
        ('Quarterly', 'Quarterly'),
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
        ('Daily', 'Daily'),
        ('Randomly', 'Randomly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount_invested = models.DecimalField(max_digits=5, decimal_places=2)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, default='Monthly')
    date_invested = models.DateField()
    description = models.TextField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    url = models.URLField(max_length=500, blank=True, null=True) 

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
