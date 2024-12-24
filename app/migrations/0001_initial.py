# Generated by Django 5.1.4 on 2024-12-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=32)),
                ('temperature', models.CharField(max_length=24)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=16)),
                ('updated_date', models.DateTimeField()),
                ('api_response', models.TextField()),
            ],
        ),
    ]
