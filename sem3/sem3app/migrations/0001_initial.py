# Generated by Django 4.2.7 on 2023-12-12 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
        migrations.CreateModel(
            name='User',
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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(blank=True, null=True)),
                ('total_price', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sem3app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sem3app.user')),
            ],
        ),
    ]