from django.db import models

class Tboperatorlist(models.Model):
    recordnum = models.BigAutoField(primary_key=True)
    employee = models.CharField(max_length=100)
    id = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tboperatorlist'

class OptDbseikeimdrcrossout(models.Model):
    ctlno = models.CharField(db_column='CTLNO', max_length=100, primary_key=True)  # Field name made lowercase.
    itmcd = models.CharField(db_column='ITMCD', max_length=20)  # Field name made lowercase.
    lotno = models.CharField(db_column='LOTNO', max_length=20)  # Field name made lowercase.
    grsqty = models.IntegerField(db_column='GRSQTY')  # Field name made lowercase.
    molder = models.IntegerField(db_column='MOLDER')  # Field name made lowercase.
    encoder = models.CharField(db_column='ENCODER', max_length=20)  # Field name made lowercase.
    inputdate = models.DateTimeField(db_column='INPUTDATE', auto_now_add=True)  # Field name made lowercase.
    moldrej = models.IntegerField(db_column='MOLDREJ')  # Field name made lowercase.
    machineno = models.CharField(db_column='MachineNo', max_length=100)  # Field name made lowercase.
    moldno = models.CharField(db_column='MOLDNO', max_length=100)  # Field name made lowercase.
    batchno = models.CharField(db_column='BATCHNO', max_length=100)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=100)  # Field name made lowercase.
    ovenstatus = models.CharField(db_column='OVENSTATUS', max_length=100)  # Field name made lowercase.
    control_status = models.IntegerField(db_column='Control_Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opt_dbseikeimdrcrossout'