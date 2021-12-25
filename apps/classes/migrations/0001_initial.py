# Generated by Django 3.2.5 on 2021-12-24 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=350, verbose_name='Class name')),
                ('class_category', models.CharField(max_length=350, verbose_name='Class category')),
                ('class_cover', models.ImageField(upload_to='uploads/class_covers', verbose_name='Class cover')),
                ('class_lessons', models.IntegerField(verbose_name='Class lessons numbers')),
                ('class_students', models.IntegerField(verbose_name='Class students')),
                ('years_range', models.CharField(max_length=350, verbose_name='Years range')),
                ('difficulty', models.CharField(max_length=350, verbose_name='IQ diffiulty')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher', verbose_name='Class teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ClassDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Description body')),
                ('image', models.ImageField(upload_to='uploads/class_descriptions_images', verbose_name='Description image')),
                ('related_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class', verbose_name='Related class')),
            ],
            options={
                'verbose_name': 'Class description',
                'verbose_name_plural': 'Class descriptions',
            },
        ),
    ]