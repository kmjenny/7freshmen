# Generated by Django 3.2.18 on 2023-02-24 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0055_auto_20230224_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ISFJ', 'ISFJ'), ('ISTJ', 'ISTJ'), ('INFP', 'INFP'), ('ESFP', 'ESFP'), ('INTP', 'INTP'), ('INFJ', 'INFJ'), ('ESTP', 'ESTP'), ('ENFJ', 'ENFJ'), ('ENFP', 'ENFP'), ('ISTP', 'ISTP'), ('INTJ', 'INTJ'), ('ENTP', 'ENTP'), ('ISFP', 'ISFP'), ('ESFJ', 'ESFJ'), ('ENTJ', 'ENTJ'), ('ESTJ', 'ESTJ')], max_length=16, null=True),
        ),
    ]
