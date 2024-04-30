# Generated by Django 4.1.7 on 2024-04-28 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='pin',
            field=models.IntegerField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='balance',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(blank=True, default=None, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user_client', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]