# Generated by Django 2.1.7 on 2020-11-06 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500, unique=True)),
                ('optiona', models.CharField(max_length=50)),
                ('optionb', models.CharField(max_length=50)),
                ('optionc', models.CharField(max_length=50)),
                ('optiond', models.CharField(max_length=50)),
                ('correct', models.CharField(max_length=10)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.technology'),
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.technology'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.technology'),
        ),
    ]
