# Generated by Django 5.1.5 on 2025-02-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_sample_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
