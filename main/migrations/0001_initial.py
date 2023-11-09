# Generated by Django 3.2.8 on 2023-11-08 08:10

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('memo', models.TextField()),
                ('duedate', models.DateField()),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=main.models.upload_image_to)),
            ],
        ),
    ]