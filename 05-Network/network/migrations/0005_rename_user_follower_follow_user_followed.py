# Generated by Django 5.0.1 on 2024-02-25 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user_follower',
            new_name='user_followed',
        ),
    ]