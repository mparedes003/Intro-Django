# Generated by Django 2.1.4 on 2018-12-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smurfs', '0002_userssmurf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smurf',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='years old'),
        ),
        migrations.AlterField(
            model_name='smurf',
            name='size',
            field=models.PositiveSmallIntegerField(verbose_name='inches'),
        ),
    ]
