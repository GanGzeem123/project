# Generated by Django 4.2.9 on 2024-01-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Racsub_app', '0005_employee_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='userlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('userpass', models.CharField(max_length=50)),
                ('useremail', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]