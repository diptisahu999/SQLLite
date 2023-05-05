from django.utils import timezone
from django.db import models



# Create your models here
class BmsBuildingMaster(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    tower_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tower_name

    class Meta():
        db_table = 'bms_building_master'


class BmsFloorMaster(models.Model):
    tower_id = models.ForeignKey(BmsBuildingMaster,on_delete=models.CASCADE,related_name='floor_data',null=True,blank=True)   ## changeses
    floor_name = models.CharField(max_length=100)
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.floor_name

    class Meta():
        db_table = 'bms_floor_master'


class BmsAreaMaster(models.Model):
    floor_data = models.ForeignKey(BmsFloorMaster,on_delete=models.CASCADE,related_name='areas_data',null=True)
    area_name = models.CharField(max_length=100)
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.area_name

    class Meta():
        db_table = 'bms_area_master '


class BmsDepartmentMaster(models.Model):
    # floor_id=models.ManyToManyField(BmsFloorMaster)
    department_name = models.CharField(max_length=100)
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_name

    class Meta():
        db_table = 'bms_department_master'


class BmsSubAreaMaster(models.Model):
    # floor_id=models.ManyToManyField(bms_floor_master, )
    # tower_details=models.ManyToManyField(bms_building_master, )
    sub_area_name = models.CharField(max_length=100)
    area_data = models.ForeignKey(BmsAreaMaster,on_delete=models.CASCADE,related_name='sub_areas_data',null=True)
    on_image_path = models.CharField(max_length=255, blank=True)
    off_image_path = models.CharField(max_length=255, blank=True)
    width = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)
    seating_capacity = models.BigIntegerField()
    devices_details = models.JSONField(default=dict, null=True, blank=True)
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_area_name

    class Meta():
        db_table = 'bms_sub_area_master'


class BmsLocker(models.Model):
    CATEGORIES = [
        ("Normal", "Normal"),
        ("Big", "Big"),
    ]

    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    category = models.CharField(max_length=100, choices=CATEGORIES , default=CATEGORIES[0][0])
    sub_area_data = models.ForeignKey(BmsSubAreaMaster,on_delete=models.CASCADE)
    locker_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.locker_name

    class Meta():
        db_table = 'bms_locker'


class BmsAccessControlRfidMaster(models.Model):
    CARD_TYPES = [
        ('No-assign', 'No-assign'),
        ('Static', 'Static'),
        ('Dynamic', 'Dynamic')
    ]

    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    user_data = models.ForeignKey(to='Authenticate.BmsUser',on_delete=models.CASCADE)
    rfid_no = models.IntegerField()
    card_type = models.CharField(max_length=100, choices=CARD_TYPES)
    access_area_data = models.ForeignKey(BmsSubAreaMaster,on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    access_start_time = models.DateField(default=timezone.now)
    access_end_time = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rfid_no)

    class Meta():
        db_table = 'bms_access_control_rfid_master'


class BmsHistory(models.Model):
    TYPES = [
        ('Newuser', 'Newuser'),
        ('Visitor', 'Visitor'),
        ('Access', 'Access'),
        ('Conference', 'Conference'),
    ]
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    user_data = models.ForeignKey(to='Authenticate.BmsUser',on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=TYPES)
    description = models.JSONField(default=dict, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

    class Meta():
        db_table = 'bms_history'


class BmsSettings(models.Model):
    module_id = models.ForeignKey(to='Authenticate.BmsModuleMaster',on_delete=models.CASCADE)
    setting_data = models.JSONField(default=dict, null=True)
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]

    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.setting_data

    class Meta():
        db_table = 'bms_settings'


class BmsHardwareTypeMaster(models.Model):
    Hardware_choice = [
        ("Relay", "Relay"),
        ("Dali", "Dali"),
        ("CoolMaster", "CoolMaster"),

    ]
    id = models.AutoField(primary_key=True, unique=True)
    hardware_name = models.CharField(
        max_length=12, choices=Hardware_choice, blank=True, null=False)
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hardware_name

    class Meta():
        db_table = 'bms_hardware_type_master'


class BmsDeviceTypeMaster(models.Model):
    hardware_type_id = models.ForeignKey(BmsHardwareTypeMaster,on_delete=models.CASCADE)
    device_slug = [("LED","LED"),
                   ("AC","AC"),
                   ("TV","TV"),
                   ("Curtain","curtain "),
                   ("PRJ","Projector"),
                   ("AVR","AVR"),
                   ("MP","MP"),
                   ("BRP","BRP"),
                   ("STB","STB"),
                   ]
    name = models.CharField(max_length=100)
    device_type_slug = models.CharField(max_length=100,blank=True)
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'bms_device_type_master'


class BmsDeviceInformation(models.Model):
    device_slug = [("LED","LED"),
                   ("AC","AC"),
                   ("TV","TV"),
                   ("Curtain","curtain "),
                   ("PRJ","Projector"),
                   ("AVR","AVR"),
                   ("MP","MP"),
                   ("BRP","BRP"),
                   ("STB","STB"),
                   ]

    is_used_STATUS = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100 ,choices=device_slug,blank=True)
    is_used = models.CharField(
        max_length=23, choices=is_used_STATUS, default=False)
    device_informations = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    create_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_user_details_date = models.DateTimeField(auto_now=True)
    # devices_details = models.ManyToManyField(bms_sub_area_master,)
    # hardware_type_id=models.ManyToManyField(Bms_hardware_type,related_name='device')

    def __str__(self):
        return str(self.device_type)

    class Meta():
        db_table = 'bms_device_information'


class BmsDeviceStatusHistory(models.Model):
    device_data = models.ForeignKey(BmsSubAreaMaster,on_delete=models.CASCADE)
    device_status = models.BooleanField(default=False)
    user_data = models.ForeignKey(to='Authenticate.BmsUser',on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_id

    class Meta():
        db_table = 'bms_device_status_history'


class BmsUserAreaCardsList(models.Model):
    user_data = models.ForeignKey(to='Authenticate.BmsUser',on_delete=models.CASCADE)
    card_id = models.IntegerField()
    card_name = models.CharField(max_length=100, blank=True)
    devices_details = models.JSONField(default=dict, null=True, blank=True)
    card_type = models.CharField(max_length=100, blank=True)
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]

    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(default=timezone.now)
    # department_id=models.ManyToManyField(bms_department_master,blank=True)
    # floor_id=models.ManyToManyRel(Bms_floor_master)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.card_name

    class Meta():
        db_table = 'bms_user_area_cards List'
