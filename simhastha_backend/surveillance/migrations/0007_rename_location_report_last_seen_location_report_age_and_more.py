# Generated by Django 5.1.1 on 2024-09-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveillance', '0006_public_user_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='location',
            new_name='last_seen_location',
        ),
        migrations.AddField(
            model_name='report',
            name='age',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], default='Male', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='name',
            field=models.CharField(default='John Doe', max_length=100),
            preserve_default=False,
        ),
    ]
