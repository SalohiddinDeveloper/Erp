# Generated by Django 5.1.6 on 2025-03-04 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'subject',
                'verbose_name_plural': 'subjects',
            },
        ),
        migrations.AlterField(
            model_name='groupmodel',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='app_groups.subjectmodel'),
        ),
    ]
