# Generated by Django 5.2.1 on 2025-06-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('prezzo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantita_disponibile', models.IntegerField()),
            ],
        ),
    ]
