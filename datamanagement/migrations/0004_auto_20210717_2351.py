# Generated by Django 3.1.2 on 2021-07-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamanagement', '0003_pricedefinitionsfordelivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedefinitionsfordelivery',
            name='additionalCostForPriceHike',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
