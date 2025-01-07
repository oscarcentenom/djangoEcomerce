# Generated by Django 5.1.3 on 2024-12-30 20:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_contacto', models.CharField(max_length=100, verbose_name='Nombres')),
                ('correo_contacto', models.CharField(max_length=100, verbose_name='Email')),
                ('asunt_contacto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('msj_contacto', models.TextField(max_length=255, verbose_name='Mensaje')),
                ('usr_contacto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'db_table': 'Contactos',
                'ordering': ['id'],
            },
        ),
    ]
