# Generated by Django 5.1.5 on 2025-01-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=140)),
                ('type', models.CharField(max_length=140)),
                ('status', models.IntegerField()),
                ('date', models.IntegerField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
