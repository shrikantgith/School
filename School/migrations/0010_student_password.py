# Generated by Django 3.0.6 on 2020-07-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0009_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
