# Generated by Django 4.2.6 on 2023-11-19 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("friends", "0003_alter_friend_credit_alter_friend_debt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="friend",
            name="date",
            field=models.DateField(blank=True, default=datetime.date(2023, 11, 19)),
        ),
    ]
