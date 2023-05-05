# Generated by Django 3.1.5 on 2023-05-05 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Device', '0001_initial'),
        ('Authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmsusersdetail',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bms_department', to='Device.bmsdepartmentmaster'),
        ),
        migrations.AddField(
            model_name='bmsusersdetail',
            name='locker_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bms_locker', to='Device.bmslocker'),
        ),
        migrations.AddField(
            model_name='bmsusersdetail',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abc', to='Authenticate.bmsuser'),
        ),
        migrations.AddField(
            model_name='bmsuserhasareaacces',
            name='building_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmsbuildingmaster'),
        ),
        migrations.AddField(
            model_name='bmsuserhasareaacces',
            name='device_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmsdeviceinformation'),
        ),
        migrations.AddField(
            model_name='bmsuserhasareaacces',
            name='floor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmsfloormaster'),
        ),
        migrations.AddField(
            model_name='bmsuserhasareaacces',
            name='sub_area_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmssubareamaster'),
        ),
        migrations.AddField(
            model_name='bmsuserhasareaacces',
            name='user_details_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsuser'),
        ),
        migrations.AddField(
            model_name='bmsuser',
            name='user_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='bms_use_type', to='Authenticate.bmsusertype'),
        ),
        migrations.AddField(
            model_name='bmsrolesdeviceinformation',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsrole'),
        ),
        migrations.AddField(
            model_name='bmsrolesdeviceinformation',
            name='subarea_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmssubareamaster'),
        ),
        migrations.AddField(
            model_name='bmsrole',
            name='permissions_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bms_module_master', to='Authenticate.bmsmodulemaster'),
        ),
    ]
