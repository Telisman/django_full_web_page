# Generated by Django 2.2 on 2021-04-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korisnici', '0009_comment_mid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Mid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
