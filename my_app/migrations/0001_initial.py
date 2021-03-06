# Generated by Django 3.1.4 on 2020-12-09 11:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateTimeField(default=django.utils.timezone.now)),
                ('passportSeries', models.IntegerField()),
                ('passportNumber', models.IntegerField()),
                ('dateOfPassportIssue', models.DateTimeField(default=django.utils.timezone.now)),
                ('departmentCodeOfThePassport', models.IntegerField()),
                ('whoIssuedThePassport', models.CharField(max_length=200)),
                ('phoneNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Premises',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monthlyFee', models.IntegerField()),
                ('square', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=2200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='rentContract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contractPeriod', models.DateTimeField(default=django.utils.timezone.now)),
                ('paymentAmount', models.IntegerField()),
                ('idClient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.client')),
            ],
        ),
    ]
