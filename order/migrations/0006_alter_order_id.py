# Generated by Django 4.2.11 on 2024-03-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_tx_ref_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.SlugField(editable=False, primary_key=True, serialize=False),
        ),
    ]
