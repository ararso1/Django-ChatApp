# Generated by Django 4.0.3 on 2022-11-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]