# Generated by Django 2.2.6 on 2019-12-22 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quetions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('questpack', models.CharField(max_length=500)),
                ('quest1', models.BooleanField(default=False)),
                ('quest2', models.BooleanField(default=False)),
                ('quest3', models.BooleanField(default=False)),
                ('quest4', models.BooleanField(default=False)),
                ('truequest', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]