# Generated by Django 5.1.7 on 2025-03-29 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_optionstrade_picture1_alter_optionstrade_trim1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionstrade',
            name='quantity',
            field=models.SmallIntegerField(),
        ),
    ]
