# Generated by Django 2.2.2 on 2019-08-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]