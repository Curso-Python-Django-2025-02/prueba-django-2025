# Generated by Django 5.1.6 on 2025-02-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='preferencias',
            field=models.TextField(blank=True, null=True),
        ),
    ]
