# Generated by Django 5.0.1 on 2024-02-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_rename_user_follower_follow_user_followed'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]