# Generated by Django 4.0.5 on 2022-06-07 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_education_achievement_alter_education_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workexperience',
            old_name='company',
            new_name='institution',
        ),
    ]