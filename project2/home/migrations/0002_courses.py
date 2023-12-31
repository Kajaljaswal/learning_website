# Generated by Django 4.2.4 on 2023-08-27 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('add_date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
