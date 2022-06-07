# Generated by Django 4.0 on 2022-06-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aboutme_contact_education_project_workexperience_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTechStach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('fa_object', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='ProffessionalSkill',
            new_name='ProgrammingLanguage',
        ),
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name_plural': 'About Me'},
        ),
    ]
