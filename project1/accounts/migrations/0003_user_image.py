# Generated by Django 2.2.2 on 2019-06-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190615_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Image',
            field=models.ImageField(default=-1.0, upload_to='profile_image'),
            preserve_default=False,
        ),
    ]
