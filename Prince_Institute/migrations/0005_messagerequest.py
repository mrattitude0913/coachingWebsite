# Generated by Django 2.1.7 on 2020-11-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prince_Institute', '0004_fee_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
