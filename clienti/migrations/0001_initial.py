# Generated by Django 5.2.1 on 2025-06-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.EmailField(max_length=254)),
                ('indirizzo', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
