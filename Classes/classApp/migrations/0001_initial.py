# Generated by Django 3.1.4 on 2020-12-20 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=50)),
                ('course_number', models.IntegerField(blank=True, max_length=20)),
                ('instructor_name', models.CharField(blank=True, max_length=50)),
                ('duration', models.FloatField(blank=True, max_length=50)),
            ],
        ),
    ]
