# Generated by Django 3.2.9 on 2021-11-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='osztaly',
            name='kor',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]