from django.contrib.gis.db import models as gis_models
from django.db.models import DO_NOTHING

from tabiri_api.apps.core.models import AdminUnitValidityModel, TimestampedModel


class Country(AdminUnitValidityModel):
    class Meta:
        managed = False
        verbose_name_plural = "Countries"

    adm0_pcode = gis_models.CharField(max_length=50, unique=True, db_column='country_code')
    adm0_en = gis_models.CharField(max_length=50, db_column='country_name')
    adm0_ref = gis_models.CharField(max_length=50, null=True, db_column='country_ref')
    adm0alt1en = gis_models.CharField(max_length=50, null=True)
    adm0alt2en = gis_models.CharField(max_length=50, null=True)
    shape_leng = gis_models.FloatField()
    shape_area = gis_models.FloatField()
    date = gis_models.DateField(auto_now_add=True)

    geom = gis_models.MultiPolygonField(srid=4326, null=True)

    def get_country_code(self):
        return self.adm0_pcode

    def get_country_name(self):
        return self.adm0_en

    def __str__(self):
        return self.adm0_en


class County(TimestampedModel):
    class Meta:
        managed = False
        verbose_name_plural = "Counties"

    objectid = gis_models.BigIntegerField()
    id_field = gis_models.BigIntegerField(null=True)
    county_cod = gis_models.BigIntegerField(unique=True, db_column='county_code')
    county_nam = gis_models.CharField(max_length=80, db_column='county_name')
    # country_code = gis_models.CharField(max_length=20, default='KE')
    const_code = gis_models.BigIntegerField(db_column='constituency_code', null=True)
    constituen = gis_models.CharField(max_length=80, db_column='constituency_name', null=True)
    shape_leng = gis_models.FloatField()
    shape_area = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326, null=True)

    country_code = gis_models.ForeignKey(Country, db_column='country_code', on_delete=gis_models.CASCADE,
                                       to_field='adm0_pcode')

    def get_county_code(self):
        return self.county_cod

    def get_county_name(self):
        return self.county_nam

    def get_country_code(self):
        return self.country_code

    def __str__(self):
        return self.county_nam


# class County(CountryRelatedModel):
#     class Meta:
#         verbose_name_plural = "Counties"
#
#     adm1_pcode = gis_models.CharField(max_length=50, unique=True, db_column='county_code')
#     adm1_en = gis_models.CharField(max_length=50, db_column='county_name')
#     adm1_ref = gis_models.CharField(max_length=50, null=True, db_column='county_ref')
#     adm1alt1en = gis_models.CharField(max_length=50, null=True)
#     adm1alt2en = gis_models.CharField(max_length=50, null=True)
#     shape_leng = gis_models.FloatField()
#     shape_area = gis_models.FloatField()
#     date = gis_models.DateField(auto_now_add=True)
#     geom = gis_models.MultiPolygonField(srid=4326, null=True)
#
#     adm0_pcode = gis_models.ForeignKey(Country, db_column='country_code', on_delete=gis_models.CASCADE, to_field='adm0_pcode')
#
#     def get_county_code(self):
#         return self.adm1_pcode
#
#     def get_county_name(self):
#         return self.adm1_en
#
#     def get_country_code(self):
#         return self.adm0_pcode
#
#     def get_country_name(self):
#         return self.adm0_en
#
#     def __str__(self):
#         return self.adm1_en


class Constituency(TimestampedModel):
    class Meta:
        managed = False
        verbose_name_plural = "Constituencies"

    objectid = gis_models.BigIntegerField()
    const_code = gis_models.BigIntegerField(unique=True, db_column='constituency_code')
    # const_code = gis_models.BigIntegerField(db_column='constituency_code')
    constituen = gis_models.CharField(max_length=80, db_column='constituency_name')
    # county_cod = gis_models.BigIntegerField(db_column='county_code')
    county_nam = gis_models.CharField(max_length=80, db_column='county_name')
    shape_leng = gis_models.FloatField()
    shape_area = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326, null=True)

    county_cod = gis_models.ForeignKey(County, db_column='county_code', on_delete=gis_models.CASCADE,
                                         to_field='county_cod')

    def __str__(self):
        managed = False
        return self.constituen


# class SubCounty(CountyRelatedModel):
#     class Meta:
#         verbose_name_plural = "SubCounties"
#
#     adm2_pcode = gis_models.CharField(max_length=50, unique=True, db_column='sub_county_code')
#     adm2_en = gis_models.CharField(max_length=50, db_column='sub_county_name')
#     adm2_ref = gis_models.CharField(max_length=50, null=True, db_column='sub_county_ref')
#     adm2alt1en = gis_models.CharField(max_length=50)
#     adm2alt2en = gis_models.CharField(max_length=50)
#     shape_leng = gis_models.FloatField()
#     shape_area = gis_models.FloatField()
#     date = gis_models.DateField(auto_now_add=True)
#     geom = gis_models.MultiPolygonField(srid=4326, null=True)
#
#     # county = gis_models.ForeignKey(County, on_delete=gis_models.CASCADE)
#     adm1_pcode = gis_models.ForeignKey(County, db_column='county_code', on_delete=gis_models.CASCADE,
#                                        to_field='adm1_pcode')
#
#     def __str__(self):
#         return self.adm2_en


# class Ward(gis_models.Model):
#     iebc_wards = gis_models.CharField(max_length=100)
#     count = gis_models.BigIntegerField()
#     first_prov = gis_models.CharField(max_length=50)
#     first_dist = gis_models.CharField(max_length=50)
#     first_divi = gis_models.CharField(max_length=50)
#     pcode = gis_models.CharField(max_length=16)
#     status = gis_models.CharField(max_length=16)
#     no = gis_models.IntegerField()
#     shape_1 = gis_models.CharField(max_length=9)
#     status_1 = gis_models.CharField(max_length=16)
#     geom = gis_models.MultiPolygonField(srid=4326)
#
#     def __str__(self):
#         return self.iebc_wards


class Ward(TimestampedModel):
    objectid = gis_models.BigIntegerField()
    name = gis_models.CharField(max_length=80, db_column='ward_name')
    # const_code = gis_models.BigIntegerField(db_column='constituency_code')
    constituen = gis_models.CharField(max_length=80, db_column='constituency_name')
    county_cod = gis_models.BigIntegerField(db_column='county_code')
    county_nam = gis_models.CharField(max_length=80, db_column='county_name')
    shape_leng = gis_models.FloatField()
    # shape_le_1 = gis_models.FloatField()
    shape_area = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326, null=True)
    ward_dhis2_id = gis_models.BigIntegerField(unique=True, null=True, default=37615001008)

    const_code = gis_models.ForeignKey(Constituency, db_column='constituency_code', on_delete=gis_models.CASCADE,
                                       to_field='const_code')

    def __str__(self):
         return self.name


class HealthFacility(gis_models.Model):
    orgunitid = gis_models.CharField(primary_key=True, max_length=60, default=37615001008)
    orgunitname = gis_models.CharField(max_length=200)
    dhis2uid = gis_models.CharField(max_length=60)
    dhis2parentid = gis_models.ForeignKey(Ward, db_column='dhis2parentid', on_delete=DO_NOTHING, default=37615001008,
                                         to_field='ward_dhis2_id')
    dhis2id = gis_models.IntegerField()
    hierarchylevel = gis_models.IntegerField(blank=True, null=True)
    aggregatedbirths = gis_models.BigIntegerField(blank=True, null=True)
    ward_name = gis_models.CharField(max_length=60, blank=True, null=True)
    ward_dhis2_parent_id = gis_models.IntegerField(blank=True, null=True)
    constituency_name = gis_models.CharField(max_length=60, blank=True, null=True)
    constituency_code = gis_models.IntegerField(blank=True, null=True)
    lat = gis_models.FloatField(blank=True, null=True)
    long = gis_models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'health_facilities'

    def __str__(self):
         return self.orgunitname


class VaccineDemandFeature(gis_models.Model):
    id = gis_models.AutoField(primary_key=True)
    orgunitid = gis_models.ForeignKey(HealthFacility, db_column='orgunitid', on_delete=gis_models.CASCADE,
                                         to_field='orgunitid', default=37615001008)
    month = gis_models.IntegerField(blank=True, null=True)
    year = gis_models.IntegerField(blank=True, null=True)
    totalbirths = gis_models.IntegerField(blank=True, null=True)
    totalchildrenvaccinated = gis_models.IntegerField(blank=True, null=True)
    bcg_wastage_rate = gis_models.FloatField(blank=True, null=True)
    tetanus_toxoid_wastage_rate = gis_models.FloatField(blank=True, null=True)
    measles_wastage_rate = gis_models.FloatField(blank=True, null=True)
    opv_wastage_rate = gis_models.FloatField(blank=True, null=True)
    pneumococal_wastage_rate = gis_models.FloatField(blank=True, null=True)
    vit_a_wastage_rate = gis_models.FloatField(blank=True, null=True)
    yellow_fever_wastage_rate = gis_models.FloatField(blank=True, null=True)
    dpt_wastage_rate = gis_models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vaccine_demand_features'
        ordering = ['month', 'year']

    def __str__(self):
        return '{} - {}'.format(self.month, self.year)


class WardVaccineDemand(gis_models.Model):
    dhis2_id = gis_models.ForeignKey(Ward, db_column='dhis2_id', on_delete=gis_models.CASCADE,
                                         to_field='ward_dhis2_id', default=37615001008)
    month = gis_models.IntegerField(blank=True, null=True)
    year = gis_models.IntegerField(blank=True, null=True)
    totalbirths = gis_models.BigIntegerField(blank=True, null=True, default=0)
    totalchildrenvaccinated = gis_models.BigIntegerField(blank=True, null=True, default=0)
    bcg_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    tetanus_toxoid_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    measles_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    opv_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    pneumococal_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    vit_a_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    yellow_fever_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    dpt_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['month', 'year']

    def __str__(self):
        return '{} - {}'.format(self.month, self.year)


class ConstituencyVaccineDemand(gis_models.Model):
    const_code = gis_models.ForeignKey(Constituency, db_column='const_code', on_delete=gis_models.CASCADE,
                                         to_field='const_code', default=37615001008)
    month = gis_models.IntegerField(blank=True, null=True)
    year = gis_models.IntegerField(blank=True, null=True)
    totalbirths = gis_models.BigIntegerField(blank=True, null=True, default=0)
    totalchildrenvaccinated = gis_models.BigIntegerField(blank=True, null=True, default=0)
    bcg_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    tetanus_toxoid_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    measles_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    opv_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    pneumococal_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    vit_a_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    yellow_fever_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    dpt_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['month', 'year']

    def __str__(self):
        return '{} - {}'.format(self.month, self.year)


class CountyVaccineDemand(gis_models.Model):
    county_cod = gis_models.ForeignKey(County, db_column='county_cod', on_delete=gis_models.CASCADE,
                                         to_field='county_cod', default=37615001008)
    month = gis_models.IntegerField(blank=True, null=True)
    year = gis_models.IntegerField(blank=True, null=True)
    totalbirths = gis_models.BigIntegerField(blank=True, null=True, default=0)
    totalchildrenvaccinated = gis_models.BigIntegerField(blank=True, null=True, default=0)
    bcg_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    tetanus_toxoid_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    measles_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    opv_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    pneumococal_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    vit_a_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    yellow_fever_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)
    dpt_vaccine_demand = gis_models.BigIntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ['month', 'year']

    def __str__(self):
        return '{} - {}'.format(self.month, self.year)
