# Generated by Django 3.1.6 on 2021-02-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='چه موقع')),
                ('job', models.CharField(max_length=300, verbose_name='چه شغلی')),
                ('description', models.TextField(verbose_name='درباره تجربتون')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('image', models.ImageField(upload_to='projects', verbose_name='عکس پروژه')),
                ('link', models.CharField(max_length=500, verbose_name='لینک پروژه')),
                ('description', models.TextField(verbose_name='توضیحات')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام من')),
                ('speciality', models.CharField(max_length=300, verbose_name='تخصص')),
                ('about', models.TextField(verbose_name='درباره من')),
                ('phone', models.CharField(max_length=100, verbose_name='موبایل')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('instagram', models.CharField(max_length=300, verbose_name='اینستاگرام')),
                ('twitter', models.CharField(max_length=300, verbose_name='توییتز')),
                ('facebook', models.CharField(max_length=300, verbose_name='فیسبوک')),
            ],
        ),
    ]