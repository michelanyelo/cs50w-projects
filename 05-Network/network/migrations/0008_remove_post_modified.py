# Generated by Django 5.0.1 on 2024-02-25 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_alter_post_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='modified',
        ),
    ]
