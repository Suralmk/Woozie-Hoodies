# Generated by Django 4.2.11 on 2024-03-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
