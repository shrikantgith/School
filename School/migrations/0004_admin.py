# Generated by Django 3.0.6 on 2020-06-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0003_student_details_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Userid', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
            ],
        ),
    ]