# Generated by Django 4.2.6 on 2023-11-19 06:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("friends", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="friend",
            old_name="date_of_credit",
            new_name="date",
        ),
        migrations.RemoveField(
            model_name="friend",
            name="date_of_debt",
        ),
    ]