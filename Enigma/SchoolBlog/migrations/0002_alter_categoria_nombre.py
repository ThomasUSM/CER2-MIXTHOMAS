# Generated by Django 4.2.1 on 2023-06-09 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(choices=[('Administrativo', 'Opción 1'), ('opcion2', 'Opción 2'), ('opcion3', 'Opción 3')], max_length=50),
        ),
    ]
