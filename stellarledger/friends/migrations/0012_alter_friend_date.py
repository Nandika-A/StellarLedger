# Generated by Django 4.2.9 on 2024-01-03 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0011_remove_expense_group_members_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2024, 1, 3)),
        ),
    ]