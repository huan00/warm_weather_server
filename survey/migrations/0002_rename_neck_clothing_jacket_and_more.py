# Generated by Django 4.2.4 on 2023-08-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothing',
            old_name='neck',
            new_name='jacket',
        ),
        migrations.RenameField(
            model_name='clothing',
            old_name='body_jacket',
            new_name='pants',
        ),
        migrations.RenameField(
            model_name='clothing',
            old_name='body_shirt',
            new_name='shirt',
        ),
        migrations.RenameField(
            model_name='clothing',
            old_name='feet',
            new_name='shoes',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='legs',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='location',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='clothing',
            name='scarf',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
