# Generated by Django 4.2.15 on 2024-08-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_bike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(max_length=255)),
                ('payment_id', models.CharField(max_length=255)),
            ],
        ),
    ]
