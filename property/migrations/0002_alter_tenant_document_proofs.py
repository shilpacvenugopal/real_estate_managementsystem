# Generated by Django 4.2.8 on 2023-12-07 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='document_proofs',
            field=models.FileField(upload_to=''),
        ),
    ]
