# Generated by Django 4.0.5 on 2022-06-02 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cam_title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='campaign_uploads/')),
                ('details', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentOnCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('special_brands', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_image/')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parts_n_Accessories_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specifications', models.TextField()),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('product_image', models.ImageField(upload_to='productImage/')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('details', models.TextField()),
                ('logo', models.ImageField(upload_to='service_logo/', verbose_name='service_logo')),
                ('service_details_image', models.ImageField(upload_to='service_details_image/', verbose_name='service_details_image')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('bike_type', models.CharField(max_length=200)),
                ('service_type', models.CharField(choices=[('Home Service', 'Home Service'), ('Go to Workshop', 'Go to Workshop')], max_length=50)),
                ('contact_number', models.CharField(max_length=20)),
                ('booking_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('additional_services', models.TextField()),
                ('Total_cost', models.IntegerField(blank=True)),
                ('status', models.CharField(choices=[('Service Processing', 'Service Processing'), ('Service Accepted', 'Service Accepted'), ('Service Confirmed', 'Service Confirmed'), ('Service Provided', 'Service Provided'), ('Service Rejected', 'Service Rejected')], default='Service Processing', max_length=20)),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_name', to='App_main.servicesmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Booking_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
