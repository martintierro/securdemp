# Generated by Django 3.1.2 on 2020-12-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20201222_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_number',
            field=models.TextField(blank=True, default='', max_length=8),
            preserve_default=False,
        ),
    ]