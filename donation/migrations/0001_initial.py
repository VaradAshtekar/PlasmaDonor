# Generated by Django 3.1.5 on 2021-04-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=10)),
                ('desc', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('gender', models.CharField(default='', max_length=6)),
                ('phone', models.IntegerField(default=0, max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('registration_date', models.DateField()),
                ('city', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=100)),
                ('blood_grp', models.CharField(max_length=2)),
                ('covid_recovery_date', models.DateField()),
            ],
        ),
    ]
