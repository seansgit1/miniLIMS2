# Generated by Django 5.1.1 on 2025-02-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_sample_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample_result',
            name='ValueNum',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
