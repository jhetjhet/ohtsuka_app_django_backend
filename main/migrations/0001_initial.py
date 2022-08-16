# Generated by Django 4.1 on 2022-08-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OptDbseikeimdrcrossout',
            fields=[
                ('ctlno', models.CharField(db_column='CTLNO', max_length=100, primary_key=True, serialize=False)),
                ('itmcd', models.CharField(db_column='ITMCD', max_length=20)),
                ('lotno', models.CharField(db_column='LOTNO', max_length=20)),
                ('grsqty', models.IntegerField(db_column='GRSQTY')),
                ('molder', models.IntegerField(db_column='MOLDER')),
                ('encoder', models.CharField(db_column='ENCODER', max_length=20)),
                ('inputdate', models.DateTimeField(auto_now_add=True, db_column='INPUTDATE')),
                ('moldrej', models.IntegerField(db_column='MOLDREJ')),
                ('machineno', models.CharField(db_column='MachineNo', max_length=100)),
                ('moldno', models.CharField(db_column='MOLDNO', max_length=100)),
                ('batchno', models.CharField(db_column='BATCHNO', max_length=100)),
                ('remarks', models.CharField(db_column='REMARKS', max_length=100)),
                ('ovenstatus', models.CharField(db_column='OVENSTATUS', max_length=100)),
                ('control_status', models.IntegerField(db_column='Control_Status')),
            ],
            options={
                'db_table': 'opt_dbseikeimdrcrossout',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tboperatorlist',
            fields=[
                ('recordnum', models.BigAutoField(primary_key=True, serialize=False)),
                ('employee', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tboperatorlist',
                'managed': False,
            },
        ),
    ]
