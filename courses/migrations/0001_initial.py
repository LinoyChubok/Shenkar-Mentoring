# Generated by Django 3.0.4 on 2020-07-09 15:47

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.CharField(max_length=4, null=True)),
                ('currentIntersted', models.PositiveIntegerField(default=0, null=True)),
                ('maxInterested', models.PositiveIntegerField(null=True)),
                ('moreInfo', models.TextField(null=True)),
                ('datePublished', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=9, null=True)),
                ('password', models.CharField(max_length=10, null=True)),
                ('Type', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('phone', phone_field.models.PhoneField(max_length=31, null=True)),
                ('about', models.TextField(null=True)),
                ('img', models.ImageField(null=True, upload_to='images/')),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.User')),
            ],
        ),
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interestedCourse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course')),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.User')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.User'),
        ),
    ]
