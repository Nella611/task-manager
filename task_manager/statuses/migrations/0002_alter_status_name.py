# Generated by Django 4.2.2 on 2023-06-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
