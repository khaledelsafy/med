# Generated by Django 3.1.7 on 2021-03-07 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20210307_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='experience',
            new_name='الخبرة',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='salary',
            new_name='المرتب',
        ),
    ]