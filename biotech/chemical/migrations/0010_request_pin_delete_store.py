# Generated by Django 4.0.1 on 2022-02-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0009_request_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='pin',
            field=models.CharField(default='aaa', max_length=3),
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]