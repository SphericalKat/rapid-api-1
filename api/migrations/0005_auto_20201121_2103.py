# Generated by Django 3.1.3 on 2020-11-21 21:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_order_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='order',
            name='expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('p', 'pending'), ('c', 'complete')], default='p', max_length=10),
        ),
    ]