# Generated by Django 5.1.7 on 2025-03-22 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=5)),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('average_down', models.BooleanField()),
                ('reason_entry', models.CharField(max_length=255)),
                ('profit', models.BooleanField()),
                ('p_and_l', models.DecimalField(decimal_places=2, max_digits=7)),
                ('trim1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('trim2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('exit_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('reason_exit', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('picture1', models.ImageField(upload_to='trade_pictures')),
                ('picture2', models.ImageField(blank=True, default=None, upload_to='trade_pictures')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
