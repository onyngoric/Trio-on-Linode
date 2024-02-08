# Generated by Django 4.1.5 on 2024-01-31 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0010_alter_ad_condition_alter_ad_delivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='phone',
        ),
        migrations.AlterField(
            model_name='ad',
            name='delivery',
            field=models.CharField(choices=[('willing to drop off', 'willing to drop off'), ('willing to ship Item', 'willing to ship Item')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='payment',
            field=models.CharField(choices=[('cash', 'cash'), ('E-Transfer', 'E-Transfer'), ('Cash & E-Transfer', 'Cash & E-Transfer')], max_length=50, null=True),
        ),
    ]
