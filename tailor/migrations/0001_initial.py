# Generated by Django 4.2.2 on 2023-06-20 15:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_headline', models.CharField(max_length=255)),
                ('blog_category', models.CharField(max_length=100)),
                ('blog_content', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ('-date_published',),
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='blog.jpg', null=True, upload_to='album_pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='catalog.jpg', upload_to='catalog_images')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogues',
                'ordering': ['product_name'],
            },
        ),
        migrations.CreateModel(
            name='Female',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_address', models.TextField(blank=True, null=True)),
                ('client_phone_number', models.CharField(max_length=11)),
                ('client_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('bust', models.PositiveIntegerField()),
                ('waist', models.PositiveIntegerField()),
                ('hips', models.PositiveIntegerField()),
                ('bust_apex', models.PositiveIntegerField()),
                ('shoulder', models.PositiveIntegerField()),
                ('neck_to_waist', models.PositiveIntegerField()),
                ('arm_length_long', models.PositiveIntegerField()),
                ('arm_length_short', models.PositiveIntegerField()),
                ('belly', models.PositiveIntegerField()),
                ('wrist', models.PositiveIntegerField()),
                ('note', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'Female',
                'verbose_name_plural': 'Female Measurements',
                'ordering': ['client_name'],
            },
        ),
        migrations.CreateModel(
            name='Male',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_address', models.TextField(blank=True, null=True)),
                ('client_phone_number', models.CharField(max_length=11)),
                ('client_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('head', models.PositiveIntegerField()),
                ('neck', models.PositiveIntegerField()),
                ('shoulder_length', models.PositiveIntegerField()),
                ('chest', models.PositiveIntegerField()),
                ('back', models.PositiveIntegerField()),
                ('arm_length_short', models.PositiveIntegerField()),
                ('arm_length_long', models.PositiveIntegerField()),
                ('biceps', models.PositiveIntegerField()),
                ('belly', models.PositiveIntegerField()),
                ('wrist', models.PositiveIntegerField()),
                ('top_length', models.PositiveIntegerField()),
                ('trouser_length', models.PositiveIntegerField()),
                ('waist', models.PositiveIntegerField()),
                ('laps', models.PositiveIntegerField()),
                ('calf', models.PositiveIntegerField()),
                ('ankle', models.PositiveIntegerField()),
                ('note', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'Male',
                'verbose_name_plural': 'Male Measurements',
                'ordering': ['client_name'],
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('logo', models.ImageField(default='receipt.jpg', upload_to='receipt_images')),
                ('unique_ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('invoice_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField()),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('item', models.ManyToManyField(blank=True, to='tailor.catalog')),
            ],
            options={
                'verbose_name': 'Receipt',
                'verbose_name_plural': 'Receipts',
                'ordering': ['unique_ID'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tailor.blog')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('-date',),
            },
        ),
    ]