# Generated by Django 2.1.2 on 2018-11-01 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutri', '0003_auto_20181031_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='height',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutri.Patient'),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='weight',
            field=models.CharField(max_length=5),
        ),
    ]