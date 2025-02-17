# Generated by Django 5.1.5 on 2025-01-25 16:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=150)),
                ('CreatedDt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Type', models.IntegerField()),
                ('CreatedDt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.AlterModelOptions(
            name='sample',
            options={'ordering': ['-CreatedDt']},
        ),
        migrations.RemoveField(
            model_name='sample',
            name='date',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='status',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='type',
        ),
        migrations.AddField(
            model_name='sample',
            name='CreatedDt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='Priority',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sample',
            name='SampleDt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='UserText1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='Identifier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
