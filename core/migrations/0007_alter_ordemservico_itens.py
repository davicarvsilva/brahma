# Generated by Django 3.2.3 on 2021-05-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210518_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='itens',
            field=models.ManyToManyField(blank=True, to='core.Item'),
        ),
    ]
