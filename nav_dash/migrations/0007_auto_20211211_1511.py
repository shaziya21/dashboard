# Generated by Django 3.0.3 on 2021-12-11 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nav_dash', '0006_auto_20211211_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('bot_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('primary_color', models.CharField(blank=True, max_length=200, null=True)),
                ('secondary_color', models.CharField(blank=True, max_length=200, null=True)),
                ('accent_color', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='GeeksModel',
        ),
    ]