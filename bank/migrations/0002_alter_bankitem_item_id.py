# Generated by Django 4.1.7 on 2023-03-29 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankitem',
            name='item_id',
            field=models.IntegerField(unique=True),
        ),
    ]