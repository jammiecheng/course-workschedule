# Generated by Django 3.1.7 on 2022-12-30 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20221230_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='stId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff'),
        ),
    ]