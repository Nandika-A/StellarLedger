# Generated by Django 4.2.6 on 2023-11-23 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("friends", "0010_expense_group_remove_pairexpenses_group_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="expense_group_members",
            name="group",
        ),
        migrations.RemoveField(
            model_name="expense_group_members",
            name="member1",
        ),
        migrations.RemoveField(
            model_name="pairexpenses",
            name="member1",
        ),
        migrations.AlterField(
            model_name="friend",
            name="date",
            field=models.DateField(blank=True, default=datetime.date(2023, 11, 23)),
        ),
        migrations.DeleteModel(
            name="Expense_group",
        ),
        migrations.DeleteModel(
            name="Expense_group_members",
        ),
        migrations.DeleteModel(
            name="PairExpenses",
        ),
    ]