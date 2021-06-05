# Generated by Django 3.2.4 on 2021-06-05 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['name'], 'verbose_name': 'категория продукта', 'verbose_name_plural': 'категории продукта'},
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_images'),
        ),
    ]