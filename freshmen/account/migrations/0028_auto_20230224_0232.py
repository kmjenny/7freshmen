# Generated by Django 3.2.18 on 2023-02-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_auto_20230224_0232'),
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
            field=models.CharField(choices=[('ISTJ', 'ISTJ'), ('INFJ', 'INFJ'), ('ISTP', 'ISTP'), ('ISFJ', 'ISFJ'), ('ISFP', 'ISFP'), ('INTP', 'INTP'), ('INFP', 'INFP'), ('ESTJ', 'ESTJ'), ('ESTP', 'ESTP'), ('ENTP', 'ENTP'), ('ESFP', 'ESFP'), ('ENFP', 'ENFP'), ('INTJ', 'INTJ'), ('ENTJ', 'ENTJ'), ('ENFJ', 'ENFJ'), ('ESFJ', 'ESFJ')], max_length=16, null=True),
        ),
    ]