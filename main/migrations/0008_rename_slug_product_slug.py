# Generated by Django 4.0.2 on 2022-02-04 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Slug',
            new_name='slug',
        ),
    ]