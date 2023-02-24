# Generated by Django 4.1.7 on 2023-02-18 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slist.item'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='list_id',
            field=models.UUIDField(),
        ),
    ]
