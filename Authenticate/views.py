from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response 
from Authenticate.models import *
from Authenticate.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated



# class LoginView(APIView):
#     def post(self,request,format=None):
#         serializer=BmsUserDetailsSerializer(data=request.data)
#         if serializer.is_valid():
#             user_email=serializer.data.get('user_email')
#             user_password=serializer.data.get('user_password')
#             user=Bms_Users.objects.filter(user_email=user_email,user_password=user_password).first()
#             if user is not None:
#                 userDetails = Bms_Users_Details.objects.all()
#                 tutorials_serializer = UserSerializer(userDetails, many=True)
#                 return Response({"data":"true","status_code": 200, "message": "Login Successfully", "response":tutorials_serializer.data})
#             else:
#                 return Response({'error':{'non_field_error':['Email or password is not valid' ]}},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  




class LoginView(APIView):
    def post(self, request, format=None):
        login_serializer=BmsUserDetailsSerializer(data=request.data)
        
        if login_serializer.is_valid():
            user_email=login_serializer.data.get('user_email')
            user_password=login_serializer.data.get('user_password')
            try:
                user=BmsUser.objects.get(user_email=user_email, user_password=user_password)
            except BmsUser.DoesNotExist:
                return Response({"status_code": 401,'error':{'User not Found':'Email or password is not valid'}},status=status.HTTP_201_CREATED)
            userDetails = BmsUser.objects.get(user_email=user.user_email) 
            tutorials_serializer = BmsUserDetailsSerializer(userDetails, many=False)
            return Response({"data":"true","status_code": 200,"message": "Login Successfully", "response":tutorials_serializer.data})
        return Response({"status_code":401,"responce":login_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
 
    
    
     

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        bms_users = BmsUser.objects.all()        
        bms_uses_serializer = BmsUserDetailsSerializer(bms_users, many=True)
        return Response({"data":"true","status_code": 200, "message": "User Lists", "response":bms_uses_serializer.data})
    
 
    elif request.method == 'POST':
        uses_serializer = BmsUserDetailsSerializer(data=request.data)
        if uses_serializer.is_valid():
            uses_serializer.save()
            # return Response(bms_uses_serializer.data, status=status.HTTP_201_CREATED)
            # return Response({"data":"true","status_code": 200, "message": "User Accounts Create Successfully"})
            return Response({"data":"true","status_code": 200, "message": "User Added Successfully", "response":uses_serializer.data})
         
        return Response({"status_code":401,"responce":uses_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
    
    elif request.method == 'DELETE':
        count = BmsUser.objects.all().delete()
        return Response({'message': '{} User was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    try: 
        bms_users = BmsUser.objects.get(pk=pk) 
    except BmsUser.DoesNotExist: 
        return Response({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bms_uses_serializer = BmsUserDetailsSerializer(bms_users) 
        # return Response(bms_uses_serializer.data) 
        return Response({"data":"true","status_code": 200, "message": "User Get Successfully", "response":bms_uses_serializer.data})
        
 
    elif request.method == 'PUT':  
        bms_uses_serializer = BmsUserDetailsSerializer(bms_users, data=request.data) 
        if bms_uses_serializer.is_valid(): 
            bms_uses_serializer.save() 
            # return Response(bms_uses_serializer.data) 
            return Response({"data":"true","status_code": 200, "message": "User Updated Successfully", "response":bms_uses_serializer.data})
            
        return Response({"status_code":401,"responce":bms_uses_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
 
    elif request.method == 'DELETE': 
        BmsUser.delete() 
        return Response({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

#role crud

    
@api_view(['GET', 'POST', 'DELETE'])
def role_list(request): 
    if request.method == 'GET':
        bms_role = BmsRole.objects.all() 
        bms_role_serializer = RoleSerializer(bms_role, many=True)
        return Response({"data":"true","status_code": 200, "message": "Role Lists", "response":bms_role_serializer.data})
        
    elif request.method == 'POST':
        role_serializer = RoleSerializer(data=request.data)
        if role_serializer.is_valid():
            user=role_serializer.save()
            # token=get_tokens_for_user(user)
            return Response({"data":"true","status_code": 200, "message": "Role Added Successfully!!","response":role_serializer.data})
            # return Response({"data":"true","status_code": 200, "message": "User role created Successfully!!",'token':token, "response":tutorial_serializer.data})
        return Response({"status_code":401,"responce":role_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsRole.objects.all().delete()
        return Response({'message': '{} Role deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk):
    try: 
        bms_role = BmsRole.objects.get(pk=pk)
    except BmsRole.DoesNotExist: 
        return Response({'message': 'The User Role does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
 
    if request.method == 'GET': 
        bms_role_serializer = RoleSerializer(bms_role) 
        return Response({"data":"true","status_code": 200, "message": "Role Get Successfully", "response":bms_role_serializer.data}) 
 
    elif request.method == 'PUT': 
        bms_role_serializer = RoleSerializer(bms_role, data=request.data) 
        if bms_role_serializer.is_valid(): 
            bms_role_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Role Updated Sucessfuly!!","response":bms_role_serializer.data}) 
        return Response({"status_code":401,"responce":bms_role_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
 
    elif request.method == 'DELETE': 
        bms_role.delete() 
        return Response({'message': 'Role was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
        
    
    
# Bms_Users_Details table crud

@api_view(['GET', 'POST', 'DELETE'])
def user_details_list(request):
    if request.method == 'GET':
        user_details = BmsUsersDetail.objects.all()
        user_details_serializer = UserSerializer(user_details, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "User Details Lists", "response":user_details_serializer.data})
 
    elif request.method == 'POST':
        details_serializer = UserSerializer(data=request.data)
        if details_serializer.is_valid():
            details_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "User Details Added Sucessfuly!!","response":details_serializer.data}) 
        return Response({"status_code":401,"responce":details_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsUsersDetail.objects.all().delete()
        return Response({'message': '{} User details was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try: 
        user_details = BmsUsersDetail.objects.get(pk=pk) 
    except BmsUsersDetail.DoesNotExist: 
        return Response({'message': 'The User details does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({'message': 'The User details does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        user_details_serializer = UserSerializer(user_details) 
        return Response({"data":"true","status_code": 200, "message": "Get Data Successfully", "response":user_details_serializer.data}) 
 
    elif request.method == 'PUT': 
        user_details_serializer = UserSerializer(user_details, data=request.data) 
        if user_details_serializer.is_valid(): 
            user_details_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "User details updated Sucessfuly!!","response":user_details_serializer.data})
        return Response({"status_code":401,"responce":user_details_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
         
 
    elif request.method == 'DELETE': 
        user_details.delete() 
        return Response({'message': 'User details deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
# Bms_Module crud

@api_view(['GET', 'POST', 'DELETE'])
def module_list(request):
    if request.method == 'GET':
        bms_module = BmsModuleMaster.objects.all()        
        bms_module_serializer = ModuleSerializer(bms_module, many=True)
        return Response({"data":"true","status_code": 200, "message": "Module Lists", "response":bms_module_serializer.data})
    
 
    elif request.method == 'POST':
        module_serializer = ModuleSerializer(data=request.data)
        if module_serializer.is_valid():
            module_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Module Added Sucessfuly!!","response":module_serializer.data}) 
        return Response({"status_code":401,"responce":module_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsModuleMaster.objects.all().delete()
        return Response({'message': '{} Module was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def module_detail(request, pk):
    try: 
        bms_module = BmsModuleMaster.objects.get(pk=pk) 
    except BmsModuleMaster.DoesNotExist: 
        return Response({'message': 'The Module does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        module_serializer = ModuleSerializer(bms_module) 
        return Response({"data":"true","status_code": 200, "message": "Role Get Successfully", "response":module_serializer.data})  
 
    elif request.method == 'PUT': 
        module_serializer = ModuleSerializer(bms_module, data=request.data) 
        if module_serializer.is_valid(): 
            module_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Module updated Sucessfuly!!","response":module_serializer.data}) 
        return Response({"status_code":401,"responce":module_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
         
 
    elif request.method == 'DELETE': 
        bms_module.delete() 
        return Response({'message': 'Module was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    

@api_view(['GET', 'POST', 'DELETE'])
def role_device_information_list(request):
    if request.method == 'GET':
        bms_module = BmsRolesDeviceInformation.objects.all()        
        bms_module_serializer = RolesDeviceInformationSerializer(bms_module, many=True)
        return Response({"data":"true","status_code": 200, "message": "Role Device Information Lists", "response":bms_module_serializer.data})
    
 
    elif request.method == 'POST':
        module_serializer = RolesDeviceInformationSerializer(data=request.data)
        if module_serializer.is_valid():
            module_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Role Device Information Added Sucessfuly!!","response":module_serializer.data}) 
        return Response({"status_code":401,"responce":module_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsRolesDeviceInformation.objects.all().delete()
        return Response({'message': '{} Module was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def role_device_information_details(request, pk):
    try:
        # bms_roles_device_information
        bms_module = BmsRolesDeviceInformation.objects.get(pk=pk) 
    except BmsModuleMaster.DoesNotExist: 
        return Response({'message': 'Role Device Information does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        module_serializer = RolesDeviceInformationSerializer(bms_module) 
        return Response({"data":"true","status_code": 200, "message": "Role Get Successfully", "response":module_serializer.data}) 
 
    elif request.method == 'PUT': 
        module_serializer = RolesDeviceInformationSerializer(bms_module, data=request.data) 
        if module_serializer.is_valid(): 
            module_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Role Device Information updated Sucessfuly!!","response":module_serializer.data}) 
        return Response({"status_code":401,"responce":module_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
         
 
    elif request.method == 'DELETE': 
        bms_module.delete() 
        return Response({"message": "Role Device Information  deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

