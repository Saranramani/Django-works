# Generated by Django 4.2.2 on 2023-06-22 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testgen', '0003_alter_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
