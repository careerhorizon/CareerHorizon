# Generated by Django 5.1 on 2024-08-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('match_score', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('function', models.CharField(blank=True, max_length=500, null=True)),
                ('schedule', models.CharField(blank=True, max_length=500, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('is_scraped', models.BooleanField(default=False)),
                ('is_premium', models.BooleanField(default=False)),
                ('premium_days', models.IntegerField(default=0)),
                ('priority_level', models.IntegerField(default=0)),
                ('apply_link', models.URLField(default='', max_length=1000)),
            ],
        ),
    ]
