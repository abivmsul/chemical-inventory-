# Generated by Django 4.0.1 on 2022-03-27 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_plantdesposedchemical_microbialdesposedchemical_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animaldesposedchemical',
            name='desposedDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='microbialdesposedchemical',
            name='desposedDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='plantdesposedchemical',
            name='desposedDate',
            field=models.DateField(null=True),
        ),
    ]
