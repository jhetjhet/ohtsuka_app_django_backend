from django.db import models

class Tboperatorlist(models.Model):
    recordnum = models.BigAutoField(primary_key=True)
    employee = models.CharField(max_length=100)
    id = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tboperatorlist'

# class OptItemmastermain(models.Model):
#     itemid = models.BigAutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
#     itemno = models.CharField(db_column='ItemNo', max_length=50)  # Field name made lowercase.
#     specificmat = models.CharField(db_column='SpecificMat', max_length=50)  # Field name made lowercase.
#     molditemno = models.CharField(db_column='MoldItemNo', max_length=50)  # Field name made lowercase.
#     moldno = models.CharField(db_column='MoldNo', max_length=50)  # Field name made lowercase.
#     moldowner = models.CharField(db_column='MoldOwner', max_length=100)  # Field name made lowercase.
#     moldsetup = models.CharField(db_column='MoldSetUp', max_length=3)  # Field name made lowercase.
#     partno = models.CharField(db_column='PartNo', max_length=50)  # Field name made lowercase.
#     partname = models.CharField(db_column='PartName', max_length=200)  # Field name made lowercase.
#     customer = models.CharField(db_column='Customer', max_length=200)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
#     producer = models.CharField(db_column='Producer', max_length=50)  # Field name made lowercase.
#     mixtureno = models.CharField(db_column='MixtureNo', max_length=50)  # Field name made lowercase.
#     materialtype = models.CharField(db_column='MaterialType', max_length=50)  # Field name made lowercase.
#     kg_shift = models.FloatField(db_column='KG_Shift')  # Field name made lowercase.
#     materiallayin = models.FloatField(db_column='MaterialLayin')  # Field name made lowercase.
#     cmno = models.CharField(db_column='CMNo', max_length=16)  # Field name made lowercase.
#     cmsupplier = models.CharField(db_column='CMSupplier', max_length=100)  # Field name made lowercase.
#     machinetype = models.CharField(db_column='MachineType', max_length=50)  # Field name made lowercase.
#     harvestingmethod = models.CharField(db_column='HarvestingMethod', max_length=100)  # Field name made lowercase.
#     orignoofcavities = models.IntegerField(db_column='OrigNoOfCavities')  # Field name made lowercase.
#     actualnoofcavities = models.IntegerField(db_column='ActualNoOfCavities')  # Field name made lowercase.
#     noshot_shift = models.IntegerField(db_column='NoShot_Shift')  # Field name made lowercase.
#     quantityshift = models.IntegerField(db_column='QuantityShift')  # Field name made lowercase.
#     subpartmoldowner = models.CharField(db_column='SubpartMoldOwner', max_length=100)  # Field name made lowercase.
#     subpartsno = models.CharField(db_column='SubpartsNo', max_length=50)  # Field name made lowercase.
#     subpartqty = models.IntegerField(db_column='SubpartQty')  # Field name made lowercase.
#     subpartsupplier = models.CharField(db_column='SubpartSupplier', max_length=200)  # Field name made lowercase.
#     adhesiveuse = models.CharField(db_column='AdhesiveUse', max_length=500)  # Field name made lowercase.
#     oven = models.CharField(db_column='Oven', max_length=10)  # Field name made lowercase.
#     specialprocess = models.CharField(db_column='SpecialProcess', max_length=50)  # Field name made lowercase.
#     subcon_wc = models.CharField(db_column='SubCon_WC', max_length=50)  # Field name made lowercase.
#     subconremarks = models.CharField(db_column='SubConRemarks', max_length=200)  # Field name made lowercase.
#     finishing1speed = models.CharField(db_column='Finishing1Speed', max_length=100)  # Field name made lowercase.
#     finishing2speed = models.CharField(db_column='Finishing2Speed', max_length=100)  # Field name made lowercase.
#     finishing3speed = models.CharField(db_column='Finishing3Speed', max_length=100)  # Field name made lowercase.
#     finishing4speed = models.CharField(db_column='Finishing4Speed', max_length=100)  # Field name made lowercase.
#     inspection1speed = models.CharField(db_column='Inspection1Speed', max_length=100)  # Field name made lowercase.
#     inspection2speed = models.CharField(db_column='Inspection2Speed', max_length=100)  # Field name made lowercase.
#     inspection3speed = models.CharField(db_column='Inspection3Speed', max_length=100)  # Field name made lowercase.
#     inspection4speed = models.CharField(db_column='Inspection4Speed', max_length=100)  # Field name made lowercase.
#     assemblyspeed = models.CharField(db_column='AssemblySpeed', max_length=100)  # Field name made lowercase.
#     specialprocspeed = models.CharField(db_column='SpecialProcSpeed', max_length=100)  # Field name made lowercase.
#     packingspeed = models.CharField(db_column='PackingSpeed', max_length=100)  # Field name made lowercase.
#     productwt = models.CharField(db_column='ProductWT', max_length=100)  # Field name made lowercase.
#     typeofplastic = models.CharField(db_column='TypeofPlastic', max_length=100)  # Field name made lowercase.
#     quantityplastic = models.CharField(db_column='QuantityPlastic', max_length=100)  # Field name made lowercase.
#     packagingtype = models.CharField(db_column='PackagingType', max_length=100)  # Field name made lowercase.
#     quantitybox = models.IntegerField(db_column='QuantityBox')  # Field name made lowercase.
#     sameproduct = models.CharField(db_column='SameProduct', max_length=200)  # Field name made lowercase.
#     use_notuse = models.IntegerField(db_column='Use_NotUse')  # Field name made lowercase.
#     inputdate = models.DateTimeField(db_column='InputDate')  # Field name made lowercase.
#     status_o = models.CharField(db_column='STATUS_O', max_length=100)  # Field name made lowercase.
#     washing = models.CharField(db_column='WASHING', max_length=100)  # Field name made lowercase.
#     noofshotperbucket = models.IntegerField(db_column='NoOfShotPerBucket')  # Field name made lowercase.
#     samplingsize = models.CharField(db_column='SamplingSize', max_length=50)  # Field name made lowercase.
#     specialqtybox = models.CharField(db_column='SpecialQtyBox', max_length=100)  # Field name made lowercase.
#     motheritemno = models.CharField(db_column='MotherItemNo', max_length=20)  # Field name made lowercase.
#     finishing1process = models.CharField(db_column='Finishing1Process', max_length=100)  # Field name made lowercase.
#     finishing2process = models.CharField(db_column='Finishing2Process', max_length=100)  # Field name made lowercase.
#     finishing3process = models.CharField(db_column='Finishing3Process', max_length=100)  # Field name made lowercase.
#     finishing4process = models.CharField(db_column='Finishing4Process', max_length=100)  # Field name made lowercase.
#     inspection1process = models.CharField(db_column='Inspection1Process', max_length=100)  # Field name made lowercase.
#     inspection2process = models.CharField(db_column='Inspection2Process', max_length=100)  # Field name made lowercase.
#     inspection3process = models.CharField(db_column='Inspection3Process', max_length=100)  # Field name made lowercase.
#     inspection4process = models.CharField(db_column='Inspection4Process', max_length=100)  # Field name made lowercase.
#     weightperbox = models.DecimalField(db_column='WeightPerBox', max_digits=9, decimal_places=3)  # Field name made lowercase.
#     weightpertube = models.DecimalField(db_column='WeightPerTube', max_digits=9, decimal_places=3)  # Field name made lowercase.
#     qtypertube = models.IntegerField(db_column='QtyPerTube')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'opt_itemmastermain'


class OptDbseikeimdrcrossout(models.Model):
    ctlno = models.CharField(db_column='CTLNO', max_length=100, primary_key=True)  # Field name made lowercase.
    itmcd = models.CharField(db_column='ITMCD', max_length=20)  # Field name made lowercase.
    lotno = models.CharField(db_column='LOTNO', max_length=20)  # Field name made lowercase.
    grsqty = models.IntegerField(db_column='GRSQTY')  # Field name made lowercase.
    molder = models.IntegerField(db_column='MOLDER')  # Field name made lowercase.
    encoder = models.CharField(db_column='ENCODER', max_length=20)  # Field name made lowercase.
    inputdate = models.DateTimeField(db_column='INPUTDATE')  # Field name made lowercase.
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

class CrossoutOperator(models.Model):
    crossout = models.CharField(max_length=100)
    operator = models.CharField(max_length=50)