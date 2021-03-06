# Generated by Django 2.1.7 on 2020-11-17 13:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Prince_Institute', '0002_auto_20201101_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='fee',
            unique_together={('course', 'student')},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('user', 'aadhar')},
        ),
    ]
