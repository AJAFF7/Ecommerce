# Generated by Django 4.2.13 on 2024-05-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_product_is_sale_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='architecture',
            field=models.CharField(default='', max_length=250),
        ),
    ]
