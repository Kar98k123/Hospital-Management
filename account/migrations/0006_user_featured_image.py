# Generated by Django 4.1.2 on 2023-03-04 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
