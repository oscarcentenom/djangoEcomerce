# Generated by Django 5.1.3 on 2025-01-09 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categ', models.CharField(max_length=20, verbose_name='Categoria')),
                ('activo_categ', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Tipo_NU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo')),
                ('activo_tipo', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'db_table': 'Tipo',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_prod', models.CharField(max_length=15, verbose_name='Ref.')),
                ('nombre_prod', models.CharField(max_length=100, verbose_name='Nombre del Articulo')),
                ('imagen_prod', models.ImageField(upload_to='ArticuloApp')),
                ('descripcion_prod', models.CharField(max_length=200)),
                ('oferta_prod', models.IntegerField(blank=True, null=True)),
                ('precio_prod', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cantidad_prod', models.IntegerField()),
                ('creado_prod', models.DateTimeField(auto_now_add=True)),
                ('actualizado_prod', models.DateTimeField(auto_now_add=True)),
                ('activo_prod', models.BooleanField()),
                ('categoria_prod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArticuloApp.categoria')),
                ('tipo_prod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArticuloApp.tipo_nu')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ImagenesSegundarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_segundarias', models.ImageField(upload_to='ArticuloApp')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='ArticuloApp.producto')),
            ],
            options={
                'verbose_name': 'ImagenesSegundaria',
                'verbose_name_plural': 'ImagenesSegundarias',
                'db_table': 'ImagenesSegundaria',
            },
        ),
    ]
