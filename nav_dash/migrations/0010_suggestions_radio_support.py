# Generated by Django 3.0.3 on 2021-12-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nav_dash', '0009_auto_20211211_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='radio_support',
            field=models.CharField(choices=[('0', 'Always'), ('1', 'Never'), ('2', 'After one failed attempt')], default='0', max_length=3),
        ),
    ]
