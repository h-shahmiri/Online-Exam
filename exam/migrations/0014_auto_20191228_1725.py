# Generated by Django 2.2.6 on 2019-12-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_auto_20191227_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
