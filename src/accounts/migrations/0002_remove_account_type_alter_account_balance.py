# Generated by Django 5.2.1 on 2025-06-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='type',
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
