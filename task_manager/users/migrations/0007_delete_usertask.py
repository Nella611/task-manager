# Generated by Django 4.2.2 on 2023-06-23 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_usertask_usertask'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserTask',
        ),
    ]