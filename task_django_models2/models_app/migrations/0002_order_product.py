# Generated by Django 4.2.7 on 2023-12-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.TextField()),
                ('adress', models.TextField()),
                ('date_of_registration', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('date_add', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
