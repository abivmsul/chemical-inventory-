# Generated by Django 4.0.1 on 2022-04-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0013_alter_request_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemical',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
