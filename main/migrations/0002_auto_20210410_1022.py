# Generated by Django 3.2 on 2021-04-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='healthline',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='policeline',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
