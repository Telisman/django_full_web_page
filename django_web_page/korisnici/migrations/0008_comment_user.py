# Generated by Django 3.1.5 on 2021-03-31 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korisnici', '0007_delete_commentusermajstor'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.TextField(blank=True, null=True),
        ),
    ]
