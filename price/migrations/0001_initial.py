# Generated by Django 3.1 on 2022-02-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=200, verbose_name='Ціна')),
                ('pc_description', models.CharField(max_length=200, verbose_name='Описання')),
            ],
            options={
                'verbose_name': 'Ціна',
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_title', models.CharField(max_length=200, verbose_name='Послуга')),
                ('pt_old_price', models.CharField(max_length=200, verbose_name='Стара ціна')),
                ('pt_new_price', models.CharField(max_length=200, verbose_name='Нова ціна')),
            ],
            options={
                'verbose_name': 'Послуги',
            },
        ),
    ]