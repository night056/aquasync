# Generated by Django 4.2.7 on 2023-11-15 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_authentication', '0001_initial'),
        ('boat_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_authentication.owner'),
        ),
    ]
