# Generated by Django 5.0.6 on 2024-06-08 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confession_app', '0003_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='confession',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='confession_app.confession'),
        ),
    ]