# Generated by Django 4.2.4 on 2023-08-24 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_date', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_date', models.CharField(max_length=50)),
                ('temperature_high', models.CharField(max_length=50)),
                ('temperature_low', models.CharField(max_length=50)),
                ('temperature_avg', models.CharField(max_length=50)),
                ('wind_mph', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=50)),
                ('feels_like', models.CharField(max_length=50)),
                ('humidity', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('survey_weather', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_date', models.CharField(max_length=50)),
                ('survey_question', models.CharField(max_length=200)),
                ('survey_answer', models.CharField(max_length=200)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hat', models.CharField(blank=True, default='', max_length=100)),
                ('neck', models.CharField(blank=True, default='', max_length=100)),
                ('body_shirt', models.CharField(max_length=100)),
                ('body_jacket', models.CharField(max_length=100)),
                ('legs', models.CharField(max_length=100)),
                ('feet', models.CharField(max_length=100)),
                ('survey_clothing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
        ),
    ]
