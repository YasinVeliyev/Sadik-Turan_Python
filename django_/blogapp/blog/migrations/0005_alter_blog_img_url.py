# Generated by Django 4.1.2 on 2022-10-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img_url',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]