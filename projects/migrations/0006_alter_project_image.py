# Generated by Django 3.2.7 on 2021-09-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_experience_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
