# Generated by Django 2.0.2 on 2019-12-03 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cereals', '0002_cereal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='protein',
            field=models.IntegerField(),
        ),
    ]
