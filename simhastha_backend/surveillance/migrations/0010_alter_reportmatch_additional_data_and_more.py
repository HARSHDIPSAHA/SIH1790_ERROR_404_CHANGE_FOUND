# Generated by Django 5.1.1 on 2024-09-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveillance', '0009_alter_report_status_reportmatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportmatch',
            name='additional_data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='reportmatch',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
