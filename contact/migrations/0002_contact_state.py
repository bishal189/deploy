# Generated by Django 4.1.5 on 2023-03-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.CharField(default=None, max_length=100),
        ),
    ]