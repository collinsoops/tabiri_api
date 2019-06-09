# Generated by Django 2.1.7 on 2019-06-06 20:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('objectid', models.BigIntegerField()),
                ('const_code', models.BigIntegerField(db_column='constituency_code', unique=True)),
                ('constituen', models.CharField(db_column='constituency_name', max_length=80)),
                ('county_cod', models.BigIntegerField(db_column='county_code')),
                ('county_nam', models.CharField(db_column='county_name', max_length=80)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Constituencies',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('validon', models.DateField(null=True)),
                ('validto', models.DateField(null=True)),
                ('adm0_pcode', models.CharField(db_column='country_code', max_length=50, unique=True)),
                ('adm0_en', models.CharField(db_column='country_name', max_length=50)),
                ('adm0_ref', models.CharField(db_column='country_ref', max_length=50, null=True)),
                ('adm0alt1en', models.CharField(max_length=50, null=True)),
                ('adm0alt2en', models.CharField(max_length=50, null=True)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('objectid', models.BigIntegerField()),
                ('id_field', models.BigIntegerField(null=True)),
                ('county_cod', models.BigIntegerField(db_column='county_code', unique=True)),
                ('county_nam', models.CharField(db_column='county_name', max_length=80)),
                ('country_code', models.CharField(default='KE', max_length=20)),
                ('const_code', models.BigIntegerField(db_column='constituency_code', null=True)),
                ('constituen', models.CharField(db_column='constituency_name', max_length=80, null=True)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('objectid', models.BigIntegerField()),
                ('name', models.CharField(db_column='ward_name', max_length=80)),
                ('const_code', models.BigIntegerField(db_column='constituency_code')),
                ('constituen', models.CharField(db_column='constituency_name', max_length=80)),
                ('county_cod', models.BigIntegerField(db_column='county_code')),
                ('county_nam', models.CharField(db_column='county_name', max_length=80)),
                ('shape_leng', models.FloatField()),
                ('shape_le_1', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]