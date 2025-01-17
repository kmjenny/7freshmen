# Generated by Django 3.2.18 on 2023-02-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0054_alter_profile_mbti'),
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
            field=models.CharField(choices=[('ISTP', 'ISTP'), ('INTP', 'INTP'), ('ENTP', 'ENTP'), ('ENFP', 'ENFP'), ('INFJ', 'INFJ'), ('INFP', 'INFP'), ('ESFJ', 'ESFJ'), ('ISTJ', 'ISTJ'), ('ESTJ', 'ESTJ'), ('ENFJ', 'ENFJ'), ('ISFJ', 'ISFJ'), ('ISFP', 'ISFP'), ('ESTP', 'ESTP'), ('INTJ', 'INTJ'), ('ESFP', 'ESFP'), ('ENTJ', 'ENTJ')], max_length=16, null=True),
        ),
    ]
