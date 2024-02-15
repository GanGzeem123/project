# Generated by Django 4.2.9 on 2024-01-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Racsub_app', '0004_rename_registeruser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_firstname', models.CharField(max_length=50)),
                ('emp_lastname', models.CharField(max_length=50)),
                ('emp_gender', models.CharField(max_length=10)),
                ('emp_tel', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]