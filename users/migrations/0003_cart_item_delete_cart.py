# Generated by Django 5.0.7 on 2024-09-17 11:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_product_time_create_product_time_update'),
        ('users', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='goods.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
                'unique_together': {('user', 'product')},
            },
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]