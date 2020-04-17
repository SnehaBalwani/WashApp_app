# Generated by Django 3.0.4 on 2020-04-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='EmailId',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='customer',
            name='LastName',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='PhoneNo',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='FirstName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
