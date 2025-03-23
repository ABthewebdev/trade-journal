from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=5)
    entry_price = models.DecimalField(decimal_places=2, max_digits=7)
    average_down = models.BooleanField()
    reason_entry = models.CharField(max_length=255)
    profit = models.BooleanField()
    p_and_l = models.DecimalField(decimal_places=2, max_digits=7)
    trim1 = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0)
    trim2 = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0)
    exit_price = models.DecimalField(decimal_places=2, max_digits=7)
    reason_exit = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    picture1 = models.ImageField(upload_to='trade_pictures')
    picture2 = models.ImageField(upload_to='trade_pictures', blank=True, default=None)