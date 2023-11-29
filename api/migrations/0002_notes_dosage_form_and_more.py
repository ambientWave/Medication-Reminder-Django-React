# Generated by Django 4.2.4 on 2023-09-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='dosage_form',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='dosage_quantity_of_units_per_time',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='dosage_unit_of_measure',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='medicine_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='regimenNote',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]