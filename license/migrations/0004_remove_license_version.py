# Generated by Django 2.1.7 on 2019-02-16 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0003_auto_20190216_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='version',
        ),
    ]
