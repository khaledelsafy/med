# Generated by Django 3.1.7 on 2021-03-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_auto_20210307_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
