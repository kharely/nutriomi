# Generated by Django 2.1.3 on 2018-11-26 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('quantity_cal', models.FloatField(max_length=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gener', models.CharField(choices=[('FE', 'Female'), ('MA', 'Male')], default='FE', max_length=2)),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateTimeField(verbose_name='date published')),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('weight', models.CharField(max_length=5)),
                ('height', models.CharField(max_length=6)),
                ('miffin', models.FloatField(max_length=5)),
                ('harris', models.FloatField(max_length=5)),
                ('valencia', models.FloatField(max_length=5)),
                ('diet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutri.Diet')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutri.Patient')),
            ],
        ),
    ]
