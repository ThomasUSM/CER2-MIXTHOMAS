# Generated by Django 4.2.1 on 2023-06-09 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolBlog', '0002_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(choices=[('declaracion', 'Declaración'), ('nota', 'Nota'), ('informe', 'Informe')], max_length=50),
        ),
    ]
