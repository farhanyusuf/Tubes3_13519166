# Generated by Django 3.2 on 2021-04-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='tipe',
            field=models.TextField(default=None),
        ),
    ]
