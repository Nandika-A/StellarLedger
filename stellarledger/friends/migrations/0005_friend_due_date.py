# Generated by Django 4.2.6 on 2023-11-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("friends", "0004_alter_friend_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="friend",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]