# Generated by Django 5.1.7 on 2025-03-31 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_optionstrade_other_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionstrade',
            name='other_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
