# Generated by Django 2.0 on 2018-03-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]
