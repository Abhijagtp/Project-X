# Generated by Django 5.0.7 on 2024-12-19 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_careerform_resume_or_portfolio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerform',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile'),
        ),
    ]