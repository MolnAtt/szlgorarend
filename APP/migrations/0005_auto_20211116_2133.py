# Generated by Django 3.2.9 on 2021-11-16 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_mtk_munkakozosseg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csoport',
            name='Tanar',
        ),
        migrations.RemoveField(
            model_name='csoport',
            name='Tantargy',
        ),
        migrations.RemoveField(
            model_name='csoport',
            name='evfolyam',
        ),
        migrations.RemoveField(
            model_name='csoport',
            name='szekcio',
        ),
    ]