# Generated by Django 2.0.7 on 2018-10-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20181008_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cert',
            name='date_expired',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cert',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='years_exp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
