# Generated by Django 4.1.7 on 2024-04-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_remove_loantransaction_loan_loantransaction_loan_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantransaction',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('success', 'success'), ('declined', 'declined')], default='active', max_length=100),
        ),
    ]