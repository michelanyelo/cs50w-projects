# Generated by Django 5.0.1 on 2024-02-24 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_is_following', to=settings.AUTH_USER_MODEL)),
                ('user_follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_is_being_followed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]