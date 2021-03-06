# Generated by Django 3.1.5 on 2021-03-10 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('korisnici', '0004_auto_20210309_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customkorisnici',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_image.png', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
