# Generated by Django 3.1 on 2022-02-22 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20220220_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusCrm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status_name', models.CharField(max_length=200, verbose_name='Назва статуса')),
            ],
            options={
                'verbose_name': 'Статус',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.statuscrm', verbose_name='статус'),
        ),
    ]
