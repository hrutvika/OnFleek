# Generated by Django 3.0.2 on 2020-06-04 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spansalon', '0004_auto_20200604_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='img',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]
