# Generated by Django 2.1.7 on 2019-06-06 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabiri_gis', '0002_auto_20190606_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituency',
            name='const_code',
            field=models.BigIntegerField(db_column='constituency_code', unique=True),
        ),
        migrations.AlterField(
            model_name='constituency',
            name='county_cod',
            field=models.ForeignKey(db_column='county_code', on_delete=django.db.models.deletion.CASCADE, to='tabiri_gis.County', to_field='county_cod'),
        ),
        migrations.AlterField(
            model_name='county',
            name='country_code',
            field=models.ForeignKey(db_column='country_code', on_delete=django.db.models.deletion.CASCADE, to='tabiri_gis.Country', to_field='adm0_pcode'),
        ),
        migrations.AlterField(
            model_name='ward',
            name='const_code',
            field=models.ForeignKey(db_column='constituency_code', on_delete=django.db.models.deletion.CASCADE, to='tabiri_gis.Constituency', to_field='const_code'),
        ),
    ]