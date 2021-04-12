# Generated by Django 3.2 on 2021-04-12 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210413_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='main.neighborhood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='main.profile'),
        ),
    ]