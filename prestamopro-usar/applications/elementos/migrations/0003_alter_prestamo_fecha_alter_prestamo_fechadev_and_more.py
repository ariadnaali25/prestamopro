# Generated by Django 4.0.5 on 2023-08-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elementos', '0002_estado_persona_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha',
            field=models.DateField(verbose_name='Fecha de prestamo'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fechadev',
            field=models.DateField(verbose_name='Fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fechaposdev',
            field=models.DateField(verbose_name='Fecha posible de devolucion'),
        ),
    ]