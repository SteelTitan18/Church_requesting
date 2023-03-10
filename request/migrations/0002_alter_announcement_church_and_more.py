# Generated by Django 4.1.3 on 2023-02-06 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcement_church', to='request.church'),
        ),
        migrations.AlterField(
            model_name='church_request',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_church', to='request.church'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestion_church', to='request.church'),
        ),
    ]
