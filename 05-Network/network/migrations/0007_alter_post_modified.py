# Generated by Django 5.0.1 on 2024-02-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_post_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(null=True),
        ),
    ]
