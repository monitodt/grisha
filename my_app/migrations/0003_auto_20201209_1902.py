# Generated by Django 3.1.4 on 2020-12-09 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20201209_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='dateOfPassportIssue',
        ),
        migrations.RemoveField(
            model_name='client',
            name='departmentCodeOfThePassport',
        ),
        migrations.RemoveField(
            model_name='client',
            name='whoIssuedThePassport',
        ),
    ]