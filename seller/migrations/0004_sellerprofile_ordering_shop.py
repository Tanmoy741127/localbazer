# Generated by Django 3.1.2 on 2021-06-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20200819_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerprofile',
            name='ordering_shop',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]