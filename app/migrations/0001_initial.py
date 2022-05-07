# Generated by Django 4.0.3 on 2022-05-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='pics')),
                ('image_200px', models.ImageField(blank=True, upload_to='pics')),
                ('image_400px', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
    ]