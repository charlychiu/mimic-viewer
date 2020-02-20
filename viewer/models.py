# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admissions(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm_id = models.IntegerField(unique=True)
    admittime = models.DateTimeField()
    dischtime = models.DateTimeField()
    deathtime = models.DateTimeField(blank=True, null=True)
    admission_type = models.CharField(max_length=50)
    admission_location = models.CharField(max_length=50)
    discharge_location = models.CharField(max_length=50)
    insurance = models.CharField(max_length=255)
    language = models.CharField(max_length=10, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    ethnicity = models.CharField(max_length=200)
    edregtime = models.DateTimeField(blank=True, null=True)
    edouttime = models.DateTimeField(blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    hospital_expire_flag = models.SmallIntegerField(blank=True, null=True)
    has_chartevents_data = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'admissions'


class Age(models.Model):
    subject_id = models.IntegerField(blank=True, null=True)
    first_admit_age = models.FloatField(blank=True, null=True)
    age_group = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'age'


class Callout(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    submit_wardid = models.IntegerField(blank=True, null=True)
    submit_careunit = models.CharField(max_length=15, blank=True, null=True)
    curr_wardid = models.IntegerField(blank=True, null=True)
    curr_careunit = models.CharField(max_length=15, blank=True, null=True)
    callout_wardid = models.IntegerField(blank=True, null=True)
    callout_service = models.CharField(max_length=10)
    request_tele = models.SmallIntegerField()
    request_resp = models.SmallIntegerField()
    request_cdiff = models.SmallIntegerField()
    request_mrsa = models.SmallIntegerField()
    request_vre = models.SmallIntegerField()
    callout_status = models.CharField(max_length=20)
    callout_outcome = models.CharField(max_length=20)
    discharge_wardid = models.IntegerField(blank=True, null=True)
    acknowledge_status = models.CharField(max_length=20)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    acknowledgetime = models.DateTimeField(blank=True, null=True)
    outcometime = models.DateTimeField()
    firstreservationtime = models.DateTimeField(blank=True, null=True)
    currentreservationtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callout'


class Caregivers(models.Model):
    row_id = models.IntegerField(primary_key=True)
    cgid = models.IntegerField(unique=True)
    label = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caregivers'


class Chartevents(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    icustay = models.ForeignKey('Icustays', models.DO_NOTHING, blank=True, null=True)
    itemid = models.ForeignKey('DItems', models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.ForeignKey(Caregivers, models.DO_NOTHING, db_column='cgid', blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents'


class Chartevents1(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_1'


class Chartevents10(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_10'


class Chartevents11(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_11'


class Chartevents12(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_12'


class Chartevents13(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_13'


class Chartevents14(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_14'


class Chartevents15(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_15'


class Chartevents16(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_16'


class Chartevents17(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_17'


class Chartevents2(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_2'


class Chartevents3(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_3'


class Chartevents4(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_4'


class Chartevents5(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_5'


class Chartevents6(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_6'


class Chartevents7(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_7'


class Chartevents8(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_8'


class Chartevents9(models.Model):
    row_id = models.IntegerField()
    subject_id = models.IntegerField()
    hadm_id = models.IntegerField(blank=True, null=True)
    icustay_id = models.IntegerField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.IntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=50, blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    error = models.IntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chartevents_9'


class Cptevents(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    costcenter = models.CharField(max_length=10)
    chartdate = models.DateTimeField(blank=True, null=True)
    cpt_cd = models.CharField(max_length=10)
    cpt_number = models.IntegerField(blank=True, null=True)
    cpt_suffix = models.CharField(max_length=5, blank=True, null=True)
    ticket_id_seq = models.IntegerField(blank=True, null=True)
    sectionheader = models.CharField(max_length=50, blank=True, null=True)
    subsectionheader = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cptevents'


class DCpt(models.Model):
    row_id = models.IntegerField(primary_key=True)
    category = models.SmallIntegerField()
    sectionrange = models.CharField(max_length=100)
    sectionheader = models.CharField(max_length=50)
    subsectionrange = models.CharField(unique=True, max_length=100)
    subsectionheader = models.CharField(max_length=255)
    codesuffix = models.CharField(max_length=5, blank=True, null=True)
    mincodeinsubsection = models.IntegerField()
    maxcodeinsubsection = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_cpt'


class DIcdDiagnoses(models.Model):
    row_id = models.IntegerField(primary_key=True)
    icd9_code = models.CharField(unique=True, max_length=10)
    short_title = models.CharField(max_length=50)
    long_title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'd_icd_diagnoses'


class DIcdProcedures(models.Model):
    row_id = models.IntegerField(primary_key=True)
    icd9_code = models.CharField(unique=True, max_length=10)
    short_title = models.CharField(max_length=50)
    long_title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'd_icd_procedures'


class DItems(models.Model):
    row_id = models.IntegerField(primary_key=True)
    itemid = models.IntegerField(unique=True)
    label = models.CharField(max_length=200, blank=True, null=True)
    abbreviation = models.CharField(max_length=100, blank=True, null=True)
    dbsource = models.CharField(max_length=20, blank=True, null=True)
    linksto = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    unitname = models.CharField(max_length=100, blank=True, null=True)
    param_type = models.CharField(max_length=30, blank=True, null=True)
    conceptid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_items'


class DLabitems(models.Model):
    row_id = models.IntegerField(primary_key=True)
    itemid = models.IntegerField(unique=True)
    label = models.CharField(max_length=100)
    fluid = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    loinc_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_labitems'


class Datetimeevents(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    icustay = models.ForeignKey('Icustays', models.DO_NOTHING, blank=True, null=True)
    itemid = models.ForeignKey(DItems, models.DO_NOTHING, db_column='itemid')
    charttime = models.DateTimeField()
    storetime = models.DateTimeField()
    cgid = models.ForeignKey(Caregivers, models.DO_NOTHING, db_column='cgid')
    value = models.DateTimeField(blank=True, null=True)
    valueuom = models.CharField(max_length=50)
    warning = models.SmallIntegerField(blank=True, null=True)
    error = models.SmallIntegerField(blank=True, null=True)
    resultstatus = models.CharField(max_length=50, blank=True, null=True)
    stopped = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datetimeevents'


class DiagnosesIcd(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    seq_num = models.IntegerField(blank=True, null=True)
    icd9_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnoses_icd'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Drgcodes(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    drg_type = models.CharField(max_length=20)
    drg_code = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    drg_severity = models.SmallIntegerField(blank=True, null=True)
    drg_mortality = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drgcodes'


class Icustays(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    icustay_id = models.IntegerField(unique=True)
    dbsource = models.CharField(max_length=20)
    first_careunit = models.CharField(max_length=20)
    last_careunit = models.CharField(max_length=20)
    first_wardid = models.SmallIntegerField()
    last_wardid = models.SmallIntegerField()
    intime = models.DateTimeField()
    outtime = models.DateTimeField(blank=True, null=True)
    los = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icustays'


class InputeventsCv(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    icustay = models.ForeignKey(Icustays, models.DO_NOTHING, blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    itemid = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amountuom = models.CharField(max_length=30, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rateuom = models.CharField(max_length=30, blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.ForeignKey(Caregivers, models.DO_NOTHING, db_column='cgid', blank=True, null=True)
    orderid = models.IntegerField(blank=True, null=True)
    linkorderid = models.IntegerField(blank=True, null=True)
    stopped = models.CharField(max_length=30, blank=True, null=True)
    newbottle = models.IntegerField(blank=True, null=True)
    originalamount = models.FloatField(blank=True, null=True)
    originalamountuom = models.CharField(max_length=30, blank=True, null=True)
    originalroute = models.CharField(max_length=30, blank=True, null=True)
    originalrate = models.FloatField(blank=True, null=True)
    originalrateuom = models.CharField(max_length=30, blank=True, null=True)
    originalsite = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inputevents_cv'


class InputeventsMv(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    icustay = models.ForeignKey(Icustays, models.DO_NOTHING, blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    itemid = models.ForeignKey(DItems, models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amountuom = models.CharField(max_length=30, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    rateuom = models.CharField(max_length=30, blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.ForeignKey(Caregivers, models.DO_NOTHING, db_column='cgid', blank=True, null=True)
    orderid = models.IntegerField(blank=True, null=True)
    linkorderid = models.IntegerField(blank=True, null=True)
    ordercategoryname = models.CharField(max_length=100, blank=True, null=True)
    secondaryordercategoryname = models.CharField(max_length=100, blank=True, null=True)
    ordercomponenttypedescription = models.CharField(max_length=200, blank=True, null=True)
    ordercategorydescription = models.CharField(max_length=50, blank=True, null=True)
    patientweight = models.FloatField(blank=True, null=True)
    totalamount = models.FloatField(blank=True, null=True)
    totalamountuom = models.CharField(max_length=50, blank=True, null=True)
    isopenbag = models.SmallIntegerField(blank=True, null=True)
    continueinnextdept = models.SmallIntegerField(blank=True, null=True)
    cancelreason = models.SmallIntegerField(blank=True, null=True)
    statusdescription = models.CharField(max_length=30, blank=True, null=True)
    comments_editedby = models.CharField(max_length=30, blank=True, null=True)
    comments_canceledby = models.CharField(max_length=40, blank=True, null=True)
    comments_date = models.DateTimeField(blank=True, null=True)
    originalamount = models.FloatField(blank=True, null=True)
    originalrate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inputevents_mv'


class Labevents(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    itemid = models.ForeignKey(DLabitems, models.DO_NOTHING, db_column='itemid')
    charttime = models.DateTimeField(blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=20, blank=True, null=True)
    flag = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labevents'


# class Microbiologyevents(models.Model):
#     row_id = models.IntegerField(primary_key=True)
#     subject = models.ForeignKey('Patients', models.DO_NOTHING)
#     hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
#     chartdate = models.DateTimeField(blank=True, null=True)
#     charttime = models.DateTimeField(blank=True, null=True)
#     spec_itemid = models.ForeignKey(DItems, models.DO_NOTHING, db_column='spec_itemid', blank=True, null=True)
#     spec_type_desc = models.CharField(max_length=100, blank=True, null=True)
#     org_itemid = models.ForeignKey(DItems, models.DO_NOTHING, db_column='org_itemid', blank=True, null=True)
#     org_name = models.CharField(max_length=100, blank=True, null=True)
#     isolate_num = models.SmallIntegerField(blank=True, null=True)
#     ab_itemid = models.ForeignKey(DItems, models.DO_NOTHING, db_column='ab_itemid', blank=True, null=True)
#     ab_name = models.CharField(max_length=30, blank=True, null=True)
#     dilution_text = models.CharField(max_length=10, blank=True, null=True)
#     dilution_comparison = models.CharField(max_length=20, blank=True, null=True)
#     dilution_value = models.FloatField(blank=True, null=True)
#     interpretation = models.CharField(max_length=5, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'microbiologyevents'


class Noteevents(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    chartdate = models.DateTimeField(blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    cgid = models.ForeignKey(Caregivers, models.DO_NOTHING, db_column='cgid', blank=True, null=True)
    iserror = models.CharField(max_length=1, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noteevents'


class Outputevents(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey('Patients', models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING, blank=True, null=True)
    icustay = models.ForeignKey(Icustays, models.DO_NOTHING, blank=True, null=True)
    charttime = models.DateTimeField(blank=True, null=True)
    itemid = models.ForeignKey(DItems, models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=30, blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.ForeignKey(Caregivers, models.DO_NOTHING, db_column='cgid', blank=True, null=True)
    stopped = models.CharField(max_length=30, blank=True, null=True)
    newbottle = models.CharField(max_length=1, blank=True, null=True)
    iserror = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outputevents'


class Patients(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject_id = models.IntegerField(unique=True)
    gender = models.CharField(max_length=5)
    dob = models.DateTimeField()
    dod = models.DateTimeField(blank=True, null=True)
    dod_hosp = models.DateTimeField(blank=True, null=True)
    dod_ssn = models.DateTimeField(blank=True, null=True)
    expire_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patients'


class Prescriptions(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Patients, models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    icustay = models.ForeignKey(Icustays, models.DO_NOTHING, blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    drug_type = models.CharField(max_length=100)
    drug = models.CharField(max_length=100)
    drug_name_poe = models.CharField(max_length=100, blank=True, null=True)
    drug_name_generic = models.CharField(max_length=100, blank=True, null=True)
    formulary_drug_cd = models.CharField(max_length=120, blank=True, null=True)
    gsn = models.CharField(max_length=200, blank=True, null=True)
    ndc = models.CharField(max_length=120, blank=True, null=True)
    prod_strength = models.CharField(max_length=120, blank=True, null=True)
    dose_val_rx = models.CharField(max_length=120, blank=True, null=True)
    dose_unit_rx = models.CharField(max_length=120, blank=True, null=True)
    form_val_disp = models.CharField(max_length=120, blank=True, null=True)
    form_unit_disp = models.CharField(max_length=120, blank=True, null=True)
    route = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescriptions'


class ProcedureeventsMv(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Patients, models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    icustay = models.ForeignKey(Icustays, models.DO_NOTHING, blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    itemid = models.ForeignKey(DItems, models.DO_NOTHING, db_column='itemid', blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    valueuom = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    locationcategory = models.CharField(max_length=30, blank=True, null=True)
    storetime = models.DateTimeField(blank=True, null=True)
    cgid = models.ForeignKey(Caregivers, models.DO_NOTHING, db_column='cgid', blank=True, null=True)
    orderid = models.IntegerField(blank=True, null=True)
    linkorderid = models.IntegerField(blank=True, null=True)
    ordercategoryname = models.CharField(max_length=100, blank=True, null=True)
    secondaryordercategoryname = models.CharField(max_length=100, blank=True, null=True)
    ordercategorydescription = models.CharField(max_length=50, blank=True, null=True)
    isopenbag = models.SmallIntegerField(blank=True, null=True)
    continueinnextdept = models.SmallIntegerField(blank=True, null=True)
    cancelreason = models.SmallIntegerField(blank=True, null=True)
    statusdescription = models.CharField(max_length=30, blank=True, null=True)
    comments_editedby = models.CharField(max_length=30, blank=True, null=True)
    comments_canceledby = models.CharField(max_length=30, blank=True, null=True)
    comments_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedureevents_mv'


class ProceduresIcd(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Patients, models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    seq_num = models.IntegerField()
    icd9_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'procedures_icd'


class Services(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Patients, models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    transfertime = models.DateTimeField()
    prev_service = models.CharField(max_length=20, blank=True, null=True)
    curr_service = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Transfers(models.Model):
    row_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Patients, models.DO_NOTHING)
    hadm = models.ForeignKey(Admissions, models.DO_NOTHING)
    icustay = models.ForeignKey(Icustays, models.DO_NOTHING, blank=True, null=True)
    dbsource = models.CharField(max_length=20, blank=True, null=True)
    eventtype = models.CharField(max_length=20, blank=True, null=True)
    prev_careunit = models.CharField(max_length=20, blank=True, null=True)
    curr_careunit = models.CharField(max_length=20, blank=True, null=True)
    prev_wardid = models.SmallIntegerField(blank=True, null=True)
    curr_wardid = models.SmallIntegerField(blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    outtime = models.DateTimeField(blank=True, null=True)
    los = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfers'
