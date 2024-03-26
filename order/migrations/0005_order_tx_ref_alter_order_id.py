# Generated by Django 4.2.11 on 2024-03-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tx_ref',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default='205717', editable=False, primary_key=True, serialize=False),
        ),
    ]
