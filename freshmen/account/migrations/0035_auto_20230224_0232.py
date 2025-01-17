# Generated by Django 3.2.18 on 2023-02-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_alter_profile_mbti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', '남성'), ('female', '여성')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ISFJ', 'ISFJ'), ('ISFP', 'ISFP'), ('ESTJ', 'ESTJ'), ('ENFJ', 'ENFJ'), ('ENTJ', 'ENTJ'), ('ENFP', 'ENFP'), ('INTJ', 'INTJ'), ('INFJ', 'INFJ'), ('ISTP', 'ISTP'), ('INFP', 'INFP'), ('INTP', 'INTP'), ('ENTP', 'ENTP'), ('ESTP', 'ESTP'), ('ISTJ', 'ISTJ'), ('ESFP', 'ESFP'), ('ESFJ', 'ESFJ')], max_length=16, null=True),
        ),
    ]
