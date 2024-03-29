# Generated by Django 3.0.5 on 2020-10-07 04:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Vaqt')),
                ('aboutschool', models.TextField(verbose_name='Maktab haqida')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('tel', models.CharField(max_length=120, verbose_name='Telefon')),
                ('starttext', models.TextField(max_length=512, verbose_name='Start bosilganda chiqadigan matn')),
                ('qoida', models.TextField(max_length=4096, verbose_name='Qoidalar')),
                ('address', models.TextField(max_length=1024, verbose_name='Manzil')),
            ],
            options={
                'verbose_name': 'Bot sozlamalari',
                'verbose_name_plural': 'Bot sozlamalari',
            },
        ),
    ]
