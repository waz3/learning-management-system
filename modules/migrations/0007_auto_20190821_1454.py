# Generated by Django 2.2.2 on 2019-08-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0006_auto_20190821_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
