# Generated by Django 4.2.6 on 2023-10-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_job_alter_user_address_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
