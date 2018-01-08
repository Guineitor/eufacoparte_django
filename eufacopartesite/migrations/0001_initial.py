# Generated by Django 2.0.1 on 2018-01-08 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import eufacopartesite.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=eufacopartesite.models.upload_localtion, width_field='width_field')),
                ('label_image', models.TextField()),
                ('url_next', models.CharField(default=None, max_length=100)),
                ('url_previuous', models.CharField(default=None, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('width_field', models.IntegerField(default=None)),
                ('height_field', models.IntegerField(default=None)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PageLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('position', models.IntegerField()),
                ('page', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=eufacopartesite.models.upload_localtion, width_field='width_field')),
                ('width_field', models.IntegerField(default=None)),
                ('height_field', models.IntegerField(default=None)),
            ],
        ),
    ]
