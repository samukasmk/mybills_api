# Generated by Django 3.0.5 on 2020-04-19 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybills', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='transfer',
            options={'ordering': ['date']},
        ),
    ]