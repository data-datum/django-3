# Generated by Django 4.0.5 on 2022-07-24 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_posteo_contenido_alter_posteo_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='contenido',
            field=models.TextField(blank=True, null=True, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog_img/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='titulo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título'),
        ),
    ]