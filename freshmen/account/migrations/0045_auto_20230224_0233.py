# Generated by Django 3.2.18 on 2023-02-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0044_alter_profile_mbti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('female', '여성'), ('male', '남성')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ISTP', 'ISTP'), ('ESFJ', 'ESFJ'), ('ESTP', 'ESTP'), ('ESFP', 'ESFP'), ('ISFJ', 'ISFJ'), ('ISFP', 'ISFP'), ('INTP', 'INTP'), ('ESTJ', 'ESTJ'), ('ENTJ', 'ENTJ'), ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP'), ('ISTJ', 'ISTJ'), ('INTJ', 'INTJ'), ('INFP', 'INFP'), ('ENTP', 'ENTP'), ('INFJ', 'INFJ')], max_length=16, null=True),
        ),
    ]
