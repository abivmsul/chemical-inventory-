# Generated by Django 4.0.1 on 2022-02-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical', '0008_requestchemical_issuedquantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
