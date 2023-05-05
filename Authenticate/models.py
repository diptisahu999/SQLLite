from django.db import models
from django.utils import timezone
from Device.models import *

class BmsModuleMaster(models.Model):
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    module_name=models.CharField(max_length=254)
    module_slug=models.CharField(max_length=254)
    status = models.CharField(max_length=100,choices=STATUS,default=STATUS[0][0])
    created_module_date=models.DateTimeField(default=timezone.now)
    updated_module_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.module_name
    
    class Meta():
        db_table='bms_module_master'
        
        
class BmsRole(models.Model):
    permissions_id=models.ForeignKey(BmsModuleMaster,on_delete=models.CASCADE,related_name='bms_module_master')
    role_name=models.CharField(max_length=100)
    device_information=models.JSONField(blank=True)
    created_role_date=models.DateTimeField(default=timezone.now)
    updated_role_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.role_name
    
    class Meta():
        db_table='bms_roles'
  
  
        
class BmsUserType(models.Model):
    USERTYPE= [
        ("Admin","Admin"),
        ("Employee","Employee"),
        ("Manager","Manager"),
        ("Visitor","Visitor"),
        
    ]
    user_type_name=models.CharField(max_length=23,choices=USERTYPE)
    type_name=models.ForeignKey(BmsRole,blank=True,on_delete=models.CASCADE,related_name='bms_roles')
    created_user_type_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.user_type_name)
    class Meta():
        db_table='bms_user_types'
        
        
            
class BmsUser(models.Model):
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    DOMAIN=[
        ("Residential","Residential"),
        ("Commercial","Commercial")
    ] 
    user_type=models.ForeignKey(BmsUserType,on_delete=models.CASCADE,related_name='bms_use_type',blank=True)
    user_email=models.EmailField()
    user_password=models.CharField(max_length=254)
    domain_type=models.CharField(max_length=22,choices=DOMAIN, blank=True)
    status = models.CharField(max_length=100,choices=STATUS, default=STATUS[0][0])
    status = models.BooleanField(default=False)
    created_user_date=models.DateTimeField(default=timezone.now)
    updated_user_date=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user_email
    class Meta():
        db_table='bms_users'        
        
            
class BmsUsersDetail(models.Model):
    # from Device.models import Bms_department_master,Bms_locker
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    VEHICLE=[
        ("YES","YES"),
        ("NO","NO")
    ]
    user_id=models.ForeignKey(BmsUser,related_name='abc',on_delete=models.CASCADE)
    department_id=models.ForeignKey(BmsDepartmentMaster,on_delete=models.CASCADE,related_name='bms_department')
    locker_id=models.ForeignKey(BmsLocker,related_name='bms_locker',on_delete=models.CASCADE)
    first_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254)
    image=models.ImageField(upload_to ='uploads/', blank=True)
    phone_no=models.CharField(max_length=16)
    birthday=models.DateField(auto_now_add=True)
    address=models.TextField(max_length=2321)
    id_proof=models.ImageField(upload_to='uplodes/',blank=True)
    visiting_card=models.ImageField(upload_to='uplodes/',blank=True)
    wallet_balance=models.CharField(max_length=909)
    shift_start_time=models.DateTimeField(auto_now=True)
    shift_end_time=models.DateTimeField(default=timezone.now)
    has_vehicle=models.CharField(max_length=23,choices=VEHICLE)
    status = models.CharField(max_length=100,choices=STATUS,default=STATUS[0][0])
    created_user_details_date=models.DateTimeField(default=timezone.now)
    updated_user_details_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
    # class Meta():
    #     db_table='bms_user_details'
        
        


class BmsUserWallet(models.Model):
    user_id=models.ForeignKey(BmsUser,on_delete=models.CASCADE)
    wallet_balance=models.CharField(max_length=23)
    created_date=models.DateTimeField(default=timezone.now)
    
    
    def __str__(self) -> str:
        return self.wallet_balance
    
    class Meta:
        db_table='bms_user_wallet'
        
        
        
class BmsUserWalletTransaction(models.Model):
    TYPE=[
        ('Initial','Initial'),
        ('Topup','Topup'),
        ('Deduct','Deduct'),   
    ]
    STATUS=[
        ("Credit","Credit"),
        ("Debit","Debit"),  
    ]
    SOURCE=[
        ("EV Charging","EV Charging"),
        ("Car Parking","Car Parking"),
        ("Food","Food"),   
    ]
    user_id=models.ForeignKey(BmsUser,on_delete=models.CASCADE)
    type=models.CharField(max_length=23,choices=TYPE)
    transaction_type=models.CharField(max_length=23,choices=STATUS)
    source=models.CharField(max_length=23,choices=SOURCE)
    amount=models.CharField(max_length=23)
    point=models.CharField(max_length=23)
    
    
    def __str__(self) -> str:
        return str(self.type)
    
    class Meta:
        db_table='bms_user_wallet_trasactions'
        
        
        
class BmsUserVehiclesDetail(models.Model):
    STATUS=[
        ("Bus","Bus"),
        ("Auto","Auto"),
        ("Cycle","Cycle"),
        ("Bicycle","Bicycle"),
        ("Car","Car"),
    ]
    EV=[
        ("true","true"),
        ("No","No"),
    ]
    user_details_id=models.ForeignKey(BmsUser,on_delete=models.CASCADE)
    type=models.CharField(max_length=23,choices=STATUS)
    vehicle_no=models.CharField(max_length=23)
    driver_name=models.CharField(max_length=23)
    driver_no=models.CharField(max_length=23)
    is_ev=models.CharField(max_length=23,choices=EV)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.driver_name
    
    class Meta:
        db_table='bms_user_viehicles_details'
        
        
class BmsUserHasAreaAcces(models.Model):
    user_details_id=models.ForeignKey(BmsUser,on_delete=models.CASCADE)
    building_id=models.ForeignKey(BmsBuildingMaster,on_delete=models.CASCADE)
    floor_id=models.ForeignKey(BmsFloorMaster,on_delete=models.CASCADE)
    sub_area_id=models.ForeignKey(BmsSubAreaMaster,on_delete=models.CASCADE)
    device_id=models.ForeignKey(BmsDeviceInformation,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.status
    
    class Meta:
        db_table='bms_user_has_area_access'
        
        
class BmsRolesDeviceInformation(models.Model):
    role_id=models.ForeignKey(BmsRole,on_delete=models.CASCADE)
    subarea_id=models.ForeignKey(BmsSubAreaMaster,on_delete=models.CASCADE)
    created_date=models.DateTimeField(default=timezone.now)
    updatated_date=models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return str(self.role_id)
    
    class Meta:
        db_table='bms_roles_device_informations'
        
    