# Generated by Django 5.1 on 2024-08-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('last_login', models.CharField()),
                ('password', models.CharField()),
                ('salt', models.CharField()),
                ('bio', models.CharField()),
                ('is_active', models.BooleanField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]
