# Generated by Django 2.1.4 on 2018-12-05 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smurfs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersSmurf',
            fields=[
                ('smurf_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='smurfs.Smurf')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('smurfs.smurf',),
        ),
    ]
