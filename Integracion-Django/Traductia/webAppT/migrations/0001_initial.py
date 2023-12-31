# Generated by Django 4.2.1 on 2023-06-12 01:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRango', models.CharField(max_length=100, verbose_name='Rango del Funcionario')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDepartamento', models.CharField(max_length=100, verbose_name='Nombre del Departamento')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
                'db_table': 'sector',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutUsuario', models.CharField(max_length=12, null=True, verbose_name='Rut')),
                ('nombreUsuario', models.CharField(max_length=12, null=True, verbose_name='Nombre')),
                ('apellidosUsuario', models.CharField(max_length=12, null=True, verbose_name='Apellidos')),
                ('user', models.CharField(default='Anonimo', max_length=12, verbose_name='Usuarios')),
                ('password', models.CharField(default='123', max_length=12, verbose_name='Password')),
                ('rango', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webAppT.rango')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='webAppT.sector')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
                'ordering': ['rango', 'sector', 'nombreUsuario'],
            },
        ),
    ]
