# Generated by Django 5.1.7 on 2025-03-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_enter_trade_user_alter_exit_trade_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='enter_trade',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
