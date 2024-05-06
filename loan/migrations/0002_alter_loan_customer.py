# Generated by Django 4.1.7 on 2024-05-04 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_id_back_alter_user_id_front_and_more'),
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='account.clientprofile'),
        ),
    ]
