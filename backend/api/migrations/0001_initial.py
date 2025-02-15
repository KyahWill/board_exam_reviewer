# Generated by Django 5.1.5 on 2025-01-27 06:26

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('_content', models.TextField(db_column='content')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('_content', models.TextField(db_column='content')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='correct_for_questions', to='api.option')),
                ('options', models.ManyToManyField(related_name='questions', to='api.option')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_asked', models.DateTimeField()),
                ('date_finished', models.DateTimeField(blank=True, null=True)),
                ('is_correct', models.BooleanField()),
                ('chosen_answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chosen_results', to='api.option')),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='correct_results', to='api.option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField()),
                ('date_finished', models.DateTimeField(blank=True, null=True)),
                ('results', models.ManyToManyField(to='api.result')),
            ],
        ),
    ]
