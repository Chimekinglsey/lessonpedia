# Generated by Django 5.0 on 2024-01-05 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_tutor_pending_contract_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='total_payment',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
