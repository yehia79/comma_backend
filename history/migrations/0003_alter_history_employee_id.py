# Generated by Django 4.2.6 on 2023-11-08 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_address_alter_user_national_id_and_more'),
        ('history', '0002_alter_history_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkouts', to='users.user'),
        ),
    ]
