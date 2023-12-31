# Generated by Django 4.2.4 on 2023-10-12 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prompts',
            fields=[
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('sensitivity_to_cold', models.CharField(choices=[('A', 'I feel cold'), ('B', 'I feel a bit cold'), ('C', 'I feel content'), ('D', 'I feel toasty'), ('E', 'I feel hot')], max_length=1)),
            ],
        ),
    ]
