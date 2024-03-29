# Generated by Django 2.2.20 on 2021-05-05 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        ('delivery_user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('contact_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bill_contact_info', to='delivery_user_profile.ContactInfo')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bill_profile', to='delivery_user_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('status', models.CharField(max_length=20)),
                ('notes', models.TextField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_bill', to='delivery_order.Bill')),
                ('item_variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item_variant', to='menu.ItemVariant')),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_payment_method', to='delivery_order.PaymentMethod')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_profile', to='delivery_user_profile.Profile')),
            ],
        ),
    ]
