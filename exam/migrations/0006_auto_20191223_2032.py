# Generated by Django 2.2.6 on 2019-12-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20191223_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='quest1',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='quest2',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='quest3',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='quest4',
        ),
        migrations.AlterField(
            model_name='questions',
            name='A',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='questions',
            name='B',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='questions',
            name='C',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='questions',
            name='D',
            field=models.CharField(max_length=500),
        ),
    ]