# Generated by Django 5.0 on 2024-03-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0011_remove_itinerary_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('num_adults', models.IntegerField()),
                ('num_children', models.IntegerField()),
                ('special_requests', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Itinerary',
        ),
    ]