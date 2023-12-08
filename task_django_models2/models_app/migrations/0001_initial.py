# Generated by Django 4.2.7 on 2023-12-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
    ]
