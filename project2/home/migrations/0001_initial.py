# Generated by Django 4.2.4 on 2023-08-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.IntegerField()),
                ('courseName', models.CharField(max_length=200)),
                ('courseDescription', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FName', models.CharField(max_length=200)),
                ('LName', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('courses', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectId', models.IntegerField()),
                ('subjectName', models.CharField(max_length=200)),
                ('subjectDescription', models.CharField(max_length=500)),
            ],
        ),
    ]
