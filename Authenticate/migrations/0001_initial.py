# Generated by Django 3.1.5 on 2023-05-05 10:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BmsModuleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=254)),
                ('module_slug', models.CharField(max_length=254)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('created_module_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_module_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bms_module_master',
            },
        ),
        migrations.CreateModel(
            name='BmsRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('device_information', models.JSONField(blank=True)),
                ('created_role_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_role_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bms_roles',
            },
        ),
        migrations.CreateModel(
            name='BmsRolesDeviceInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'bms_roles_device_informations',
            },
        ),
        migrations.CreateModel(
            name='BmsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=254)),
                ('domain_type', models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Commercial', 'Commercial')], max_length=22)),
                ('status', models.BooleanField(default=False)),
                ('created_user_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_user_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bms_users',
            },
        ),
        migrations.CreateModel(
            name='BmsUserHasAreaAcces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'bms_user_has_area_access',
            },
        ),
        migrations.CreateModel(
            name='BmsUsersDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
                ('phone_no', models.CharField(max_length=16)),
                ('birthday', models.DateField(auto_now_add=True)),
                ('address', models.TextField(max_length=2321)),
                ('id_proof', models.ImageField(blank=True, upload_to='uplodes/')),
                ('visiting_card', models.ImageField(blank=True, upload_to='uplodes/')),
                ('wallet_balance', models.CharField(max_length=909)),
                ('shift_start_time', models.DateTimeField(auto_now=True)),
                ('shift_end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('has_vehicle', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=23)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('created_user_details_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_user_details_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BmsUserWalletTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Initial', 'Initial'), ('Topup', 'Topup'), ('Deduct', 'Deduct')], max_length=23)),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=23)),
                ('source', models.CharField(choices=[('EV Charging', 'EV Charging'), ('Car Parking', 'Car Parking'), ('Food', 'Food')], max_length=23)),
                ('amount', models.CharField(max_length=23)),
                ('point', models.CharField(max_length=23)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsuser')),
            ],
            options={
                'db_table': 'bms_user_wallet_trasactions',
            },
        ),
        migrations.CreateModel(
            name='BmsUserWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_balance', models.CharField(max_length=23)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsuser')),
            ],
            options={
                'db_table': 'bms_user_wallet',
            },
        ),
        migrations.CreateModel(
            name='BmsUserVehiclesDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Bus', 'Bus'), ('Auto', 'Auto'), ('Cycle', 'Cycle'), ('Bicycle', 'Bicycle'), ('Car', 'Car')], max_length=23)),
                ('vehicle_no', models.CharField(max_length=23)),
                ('driver_name', models.CharField(max_length=23)),
                ('driver_no', models.CharField(max_length=23)),
                ('is_ev', models.CharField(choices=[('true', 'true'), ('No', 'No')], max_length=23)),
                ('status', models.BooleanField(default=False)),
                ('user_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsuser')),
            ],
            options={
                'db_table': 'bms_user_viehicles_details',
            },
        ),
        migrations.CreateModel(
            name='BmsUserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type_name', models.CharField(choices=[('Admin', 'Admin'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('Visitor', 'Visitor')], max_length=23)),
                ('created_user_type_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('type_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='bms_roles', to='Authenticate.bmsrole')),
            ],
            options={
                'db_table': 'bms_user_types',
            },
        ),
    ]
