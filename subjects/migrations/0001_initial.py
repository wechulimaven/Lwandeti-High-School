# Generated by Django 2.2.18 on 2021-03-16 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=191)),
                ('subject_code', models.CharField(max_length=191)),
                ('subject_photo', models.ImageField(upload_to='subjects')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('formclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Formclass')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectSyllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus', models.TextField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='CompulsorySubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
            ],
            options={
                'verbose_name_plural': 'CompulsorySubjects',
            },
        ),
    ]
