# Generated by Django 4.2.2 on 2023-06-21 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokenapp', '0002_authenticate_delete_mytable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Authenticate',
        ),
    ]
