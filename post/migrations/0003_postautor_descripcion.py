# Generated by Django 3.1.7 on 2021-03-23 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210322_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='postautor',
            name='descripcion',
            field=models.TextField(default=''),
        ),
    ]
