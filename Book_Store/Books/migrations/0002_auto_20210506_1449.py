# Generated by Django 3.1.4 on 2021-05-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Title',
            field=models.CharField(default='', max_length=122),
        ),
    ]