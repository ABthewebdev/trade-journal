# Generated by Django 5.1.7 on 2025-03-24 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_trade_entry_time_alter_trade_exit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='trim1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='trade',
            name='trim2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
    ]
