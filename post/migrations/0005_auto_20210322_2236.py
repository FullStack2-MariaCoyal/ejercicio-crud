# Generated by Django 3.1.7 on 2021-03-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210322_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postautor',
            name='nombreAutor',
            field=models.CharField(default='', max_length=255),
        ),
    ]
