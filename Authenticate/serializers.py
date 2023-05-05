from rest_framework import serializers 
from Authenticate.models import BmsModuleMaster,BmsRole,BmsUserType,BmsUser,BmsUsersDetail,BmsRolesDeviceInformation
from Device.models import BmsDepartmentMaster,BmsLocker




class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=BmsModuleMaster
        fields='__all__'
 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=BmsRole
        fields=['id','role_name','permissions_id']
        
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BmsUserType
        fields=['id','user_type_name']        
        
        
class DepertmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=BmsDepartmentMaster
        fields=['department_name'] 
        
class lockerSerializer(serializers.ModelSerializer):
    class Meta:
        model=BmsLocker
        fields=['locker_name']
         
class BmsUserSerializer(serializers.ModelSerializer):
    # user_type_id=UserTypeSerializer(many=True,read_only=True)
    # role_id=RoleSerializer(many=True,read_only=True)
    locker_id=lockerSerializer(many=True,read_only=True)
    class Meta:
        model = BmsUsersDetail
        fields = '__all__'
        
class BmsUserDetailsSerializer(serializers.ModelSerializer):
    # role_id=RoleSerializer(many=True,read_only=True)
    # user_details=BmsUserSerializer(many=True,read_only=True)
    # department_id=DepertmentSerializer(many=True,read_only=True)
    # locker_id=lockerSerializer(many=True,read_only=True)
        
    
    class Meta:
        # role_id=RoleSerializer(many=True,read_only=True)
        # user_details=BmsUserSerializer(many=True,read_only=True)
        # department_id=DepertmentSerializer(many=True,read_only=True)
        # locker_id=lockerSerializer(many=True,read_only=True)
        model = BmsUser
        fields = '__all__'
        depth=10
        



# user registation        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsUsersDetail
        fields = '__all__'
        
        
        
# #user Views
# class Manage_user_view(serializers.ModelSerializer):
#     class Meta:
#         model = '__all__'
        
        
class RolesDeviceInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=BmsRolesDeviceInformation
        fields = '__all__'
        depth=10
                