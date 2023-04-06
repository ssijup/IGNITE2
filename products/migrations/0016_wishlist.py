# Generated by Django 4.1.5 on 2023-04-03 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_bannervedio_banvedio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_prod_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
                ('wish_user_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.userdetails')),
                ('wish_varoptio_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.variantoptions')),
            ],
        ),
    ]