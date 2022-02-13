# Generated by Django 3.2.9 on 2022-02-12 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='soni')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='categoriya nomi')),
                ('slug', models.SlugField(max_length=25, verbose_name='*')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='nomi')),
                ('slug', models.SlugField(max_length=25, verbose_name='*')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='Product image')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('description', models.TextField(verbose_name='About product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=25, verbose_name='buyurtmachi')),
                ('tel', models.PositiveIntegerField(default=0, verbose_name='tel')),
                ('is_arrived', models.BooleanField(default=False)),
                ('order', models.ManyToManyField(to='main.Cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='main.Product'),
        ),
    ]
