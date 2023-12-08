# Generated by Django 4.2.8 on 2023-12-06 17:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('features', models.TextField()),
            ],
            options={
                'db_table': '"property_details"',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('document_proofs', models.TextField()),
            ],
            options={
                'db_table': '"property_tenant"',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_type', models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], max_length=4)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
            options={
                'db_table': '"property_units"',
            },
        ),
        migrations.CreateModel(
            name='RentalInformation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('agreement_end_date', models.DateField()),
                ('monthly_rent_date', models.DateField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.tenant')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.unit')),
            ],
            options={
                'db_table': '"property_rental_information"',
            },
        ),
    ]