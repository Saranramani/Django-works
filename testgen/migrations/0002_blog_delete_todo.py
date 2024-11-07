# Generated by Django 4.2.2 on 2023-06-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testgen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
