# Generated by Django 3.0.4 on 2020-04-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200415_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Password',
            field=models.CharField(default='', max_length=120),
        ),
    ]
