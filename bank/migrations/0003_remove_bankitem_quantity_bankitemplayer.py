# Generated by Django 4.1.7 on 2023-04-01 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_alter_bankitem_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankitem',
            name='quantity',
        ),
        migrations.CreateModel(
            name='BankItemPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bank_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bankitem')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.player')),
            ],
        ),
    ]
