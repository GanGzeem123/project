# Generated by Django 4.2.9 on 2024-01-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Racsub_app', '0008_userlist_age_userlist_first_name_userlist_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='status',
            field=models.CharField(blank=True, choices=[('n', 'ออนไลน์'), ('f', 'ออฟไลน์')], max_length=1, null=True),
        ),
    ]
