# Generated by Django 3.2 on 2021-04-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='general'),
            preserve_default=False,
        ),
    ]