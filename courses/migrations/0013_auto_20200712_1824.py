# Generated by Django 3.0.4 on 2020-07-12 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20200712_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=100, null=True)),
                ('courseYear', models.CharField(max_length=10, null=True)),
                ('currentIntersted', models.PositiveIntegerField(default=0)),
                ('maxInterested', models.PositiveIntegerField(default=1)),
                ('moreInfo', models.TextField(null=True)),
                ('datePublished', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mentorcourse',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='Type',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='interestedstudent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.UserInfo'),
        ),
        migrations.AlterField(
            model_name='interestedstudent',
            name='Course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
        migrations.DeleteModel(
            name='MentorCourse',
        ),
    ]
