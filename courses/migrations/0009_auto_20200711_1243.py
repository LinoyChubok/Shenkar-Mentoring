# Generated by Django 3.0.4 on 2020-07-11 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20200710_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorcourse',
            name='mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.User'),
        ),
    ]
