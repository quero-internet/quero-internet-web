# Generated by Django 2.1.7 on 2019-04-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190424_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='observacoes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
