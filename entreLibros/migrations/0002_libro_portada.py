# Generated by Django 5.0.6 on 2024-06-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entreLibros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas/'),
        ),
    ]
