# Generated by Django 3.1.3 on 2020-12-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20201216_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='under_title',
            field=models.CharField(blank=True, default=' ', max_length=255, null=True),
        ),
    ]
