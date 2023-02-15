# Generated by Django 4.1.7 on 2023-02-14 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MallList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('list_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('list_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(default='available', max_length=20)),
                ('buy_day', models.DateField(null=True)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slist.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slist.malllist'),
        ),
    ]
