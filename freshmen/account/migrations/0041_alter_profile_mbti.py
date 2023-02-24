# Generated by Django 3.2.18 on 2023-02-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0040_auto_20230224_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti',
            field=models.CharField(choices=[('ESTP', 'ESTP'), ('ENTP', 'ENTP'), ('ESFP', 'ESFP'), ('ENFP', 'ENFP'), ('ISFJ', 'ISFJ'), ('INFJ', 'INFJ'), ('ESFJ', 'ESFJ'), ('ISTJ', 'ISTJ'), ('ESTJ', 'ESTJ'), ('ENFJ', 'ENFJ'), ('ISTP', 'ISTP'), ('INTP', 'INTP'), ('INFP', 'INFP'), ('ENTJ', 'ENTJ'), ('INTJ', 'INTJ'), ('ISFP', 'ISFP')], max_length=16, null=True),
        ),
    ]