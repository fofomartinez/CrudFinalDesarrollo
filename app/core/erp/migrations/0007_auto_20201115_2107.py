# Generated by Django 3.1.3 on 2020-11-16 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_equipos_marc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipos',
            name='pvp',
        ),
        migrations.AddField(
            model_name='equipos',
            name='existencia',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Existencia'),
        ),
        migrations.AlterField(
            model_name='equipos',
            name='marc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.marca', verbose_name='Marca'),
        ),
    ]