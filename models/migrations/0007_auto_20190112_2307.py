# Generated by Django 2.1.5 on 2019-01-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_auto_20190112_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='image',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='image',
        ),
        migrations.AddField(
            model_name='promotion',
            name='image_url',
            field=models.CharField(default='#', max_length=350),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image_url',
            field=models.CharField(default='#', max_length=350),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_url',
            field=models.CharField(default='#', max_length=250),
        ),
    ]