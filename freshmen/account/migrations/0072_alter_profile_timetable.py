# Generated by Django 4.1.6 on 2023-02-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0071_alter_profile_gender_alter_profile_live_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timetable',
            field=models.ImageField(blank=True, null=True, upload_to='timetable/'),
        ),
    ]
