# Generated by Django 4.0.1 on 2022-02-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_department_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custodian',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]