# Generated by Django 4.0.2 on 2022-02-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_order_options_order_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
