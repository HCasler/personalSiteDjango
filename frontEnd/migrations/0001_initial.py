# Generated by Django 4.2.4 on 2023-09-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('lastUpdated', models.DateTimeField(max_length=60000)),
                ('text', models.TextField()),
            ],
        ),
    ]