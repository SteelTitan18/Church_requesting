# Generated by Django 4.1.7 on 2023-02-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_rename_church_announcement_announcement_church_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='tags',
        ),
    ]
