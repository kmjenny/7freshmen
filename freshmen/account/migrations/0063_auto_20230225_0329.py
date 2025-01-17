# Generated by Django 3.2.18 on 2023-02-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0062_auto_20230225_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='drink',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favfood',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hometown',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='live',
            field=models.CharField(choices=[('N', '무'), ('None', 'None'), ('Y', '유')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ESTJ', 'ESTJ'), ('ENFJ', 'ENFJ'), ('ENTP', 'ENTP'), ('INTJ', 'INTJ'), ('ESFJ', 'ESFJ'), ('ISTP', 'ISTP'), ('ISFJ', 'ISFJ'), ('INTP', 'INTP'), ('ESFP', 'ESFP'), ('INFP', 'INFP'), ('ENTJ', 'ENTJ'), ('ISFP', 'ISFP'), ('ISTJ', 'ISTJ'), ('ENFP', 'ENFP'), ('ESTP', 'ESTP'), ('INFJ', 'INFJ')], max_length=16, null=True),
        ),
    ]
