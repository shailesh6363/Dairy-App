# Generated by Django 3.0.5 on 2020-04-06 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20200405_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entries',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
