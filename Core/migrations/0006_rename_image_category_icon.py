# Generated by Django 4.1.7 on 2023-12-30 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_remove_ads_category_id_ads_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='icon',
        ),
    ]
