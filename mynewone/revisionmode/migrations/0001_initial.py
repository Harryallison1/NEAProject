# Generated by Django 5.0.7 on 2025-02-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('correct_answer', models.CharField(max_length=255)),
                ('wrong_answer1', models.CharField(max_length=255)),
                ('wrong_answer2', models.CharField(max_length=255)),
                ('wrong_answer3', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
            ],
        ),
    ]
