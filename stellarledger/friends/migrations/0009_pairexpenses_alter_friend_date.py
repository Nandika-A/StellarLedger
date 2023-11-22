# Generated by Django 4.2.6 on 2023-11-22 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("friends", "0008_usergroup_paid"),
    ]

    operations = [
        migrations.CreateModel(
            name="PairExpenses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("group_name", models.CharField(max_length=10, unique=True)),
                ("member1", models.CharField(max_length=10)),
                ("member2", models.CharField(max_length=10)),
                (
                    "pay1to2",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0.0, max_digits=10
                    ),
                ),
                ("title", models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name="friend",
            name="date",
            field=models.DateField(blank=True, default=datetime.date(2023, 11, 22)),
        ),
    ]