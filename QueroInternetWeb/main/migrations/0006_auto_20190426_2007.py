# Generated by Django 2.2 on 2019-04-27 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190422_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='data_e_hora',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='observacoes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
