# Generated by Django 5.2.1 on 2025-07-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_type_alter_account_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
