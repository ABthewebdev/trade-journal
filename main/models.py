from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Enter_Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)
    def __str__(self):
        return self.reason

class Exit_Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.reason

class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=5)
    long = models.BooleanField(default=None)
    short = models.BooleanField(default=None)
    entry_price = models.DecimalField(decimal_places=2, max_digits=7)
    average_down = models.BooleanField()
    reasons_entry = models.ManyToManyField(Enter_Trade, related_name='trades_as_entry1')
    profit = models.BooleanField()
    loss = models.BooleanField(default=None)
    p_and_l = models.DecimalField(decimal_places=2, max_digits=7)
    trim1 = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    trim2 = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    exit_price = models.DecimalField(decimal_places=2, max_digits=7)
    reasons_exit = models.ManyToManyField(Exit_Trade, related_name='trades_as_exit1')
    date = models.DateField()
    entry_time = models.TimeField()
    exit_time = models.TimeField()
    picture1 = models.ImageField(upload_to='trade_pictures/', blank=True, default='chart.png')
    picture2 = models.ImageField(upload_to='trade_pictures/', blank=True, default=None)
    quantity = models.SmallIntegerField(default=1)
    other_notes = models.TextField()
class OptionsTrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=5)
    strike_price = models.BigIntegerField()
    call = models.BooleanField()
    put = models.BooleanField()
    stock_price = models.DecimalField(decimal_places=2, max_digits=7)
    option_price = models.DecimalField(decimal_places=2, max_digits=5)
    reasons_entry = models.ManyToManyField(Enter_Trade, related_name='trades_as_entry2')
    profit = models.BooleanField()
    loss = models.BooleanField()
    p_and_l = models.DecimalField(decimal_places=2, max_digits=8)
    trim1 = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    trim2 = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    exit_option_price = models.DecimalField(decimal_places=2, max_digits=5)
    reasons_exit = models.ManyToManyField(Exit_Trade, related_name='trades_as_exit2')
    date = models.DateField()
    entry_time = models.TimeField()
    exit_time = models.TimeField()
    picture1 = models.ImageField(upload_to='trade_pictures/', blank=True, null=True, default='chart_UqV2wpr.png')
    picture2 = models.ImageField(upload_to='trade_pictures/', blank=True, null=True)
    quantity = models.SmallIntegerField()
    other_notes = models.TextField(blank=True, null=True)