# Generated by Django 4.0.1 on 2022-04-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0009_alter_animaldesposedchemical_temprature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalstore',
            name='cabinate',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='animalstore',
            name='shelf',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantstore',
            name='cabinate',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='plantstore',
            name='shelf',
            field=models.CharField(default='-', max_length=100),
        ),
    ]