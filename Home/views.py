from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import pyrebase,os
from zipfile import ZipFile
from django.http import StreamingHttpResponse

from Home.models import Role,Faculty,User,Contribution,FileType
from Home.serializers import RoleSerializer,FacultySerializer,ContributionSerializer,FileTypeSerializer,UserSerializer
from rest_framework.decorators import api_view

config = {
    "apiKey": "AIzaSyBTJ0B6Nh-bcsGFgVmBqKE15RwrlYXLF7M",
    "authDomain": "comp1640-976c9.firebaseapp.com",
    "databaseURL": "https://comp1640-976c9-default-rtdb.firebaseio.com",
    "projectId": "comp1640-976c9",
    "storageBucket": "comp1640-976c9.appspot.com",
    "messagingSenderId": "880677718380",
    "appId": "1:880677718380:web:5fb02ddbd488292d204b49",
    "measurementId": "G-BBQ0KH6Z8M",
    "serviceAccount": "Home/serviceAccountKey.json",
}

# Role REST API
@api_view(['GET', 'POST', 'DELETE'])
def role_list(request):
    if request.method == 'GET':
        roles = Role.objects.all()

        title = request.query_params.get('role_name')
        if title is not None:
            roles = roles.filter(role_name__icontains=title)

        roles_serializer = RoleSerializer(roles, many=True)
        return JsonResponse(roles_serializer.data, safe=False)

    elif request.method == 'POST':
        role_data = JSONParser().parse(request)
        roles_serializer = RoleSerializer(data=role_data)
        if roles_serializer.is_valid():
            roles_serializer.save()
            return JsonResponse(roles_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(roles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Role.objects.all().delete()
        return JsonResponse({'message': '{} Roles were deleted successfully'.format(count[0])}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def role_detail(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return JsonResponse({'message': 'The role does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        role_serializer = RoleSerializer(role)
        return JsonResponse(role_serializer.data)

    elif request.method == 'PUT':
        role_data = JSONParser().parse(request)
        role_serializer = RoleSerializer(role, data=role_data)
        if role_serializer.is_valid():
            role_serializer.save()
            return JsonResponse(role_serializer.data)
        return JsonResponse(role_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        role.delete()
        return JsonResponse({'message': 'Role was deleted successfully!'}, status=status.HTTP_200_OK)

# Faculty REST API
@api_view(['GET', 'POST', 'DELETE'])
def faculty_list(request):
    if request.method == 'GET':
        faculties = Faculty.objects.all()

        title = request.query_params.get('faculty_name', None)
        if title is not None:
            faculties = faculties.filter(faculty_name__icontains=title)

        faculties_serializer = FacultySerializer(faculties, many=True)
        return JsonResponse(faculties_serializer.data, safe=False)

    elif request.method == 'POST':
        faculty_data = JSONParser().parse(request)
        faculties_serializer = FacultySerializer(data=faculty_data)
        if faculties_serializer.is_valid():
            faculties_serializer.save()
            return JsonResponse(faculties_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(faculties_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Faculty.objects.all().delete()
        return JsonResponse({'message': '{} Faculties were deleted successfully'.format(count[0])}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def faculty_detail(request, pk):
    try:
        faculty = Faculty.objects.get(pk=pk)
    except Faculty.DoesNotExist:
        return JsonResponse({'message': 'The faculty does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        faculty_serializer = FacultySerializer(faculty)
        return JsonResponse(faculty_serializer.data)

    elif request.method == 'PUT':
        faculty_data = JSONParser().parse(request)
        faculty_serializer = FacultySerializer(faculty, data=faculty_data)
        if faculty_serializer.is_valid():
            faculty_serializer.save()
            return JsonResponse(faculty_serializer.data)
        return JsonResponse(faculty_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        faculty.delete()
        return JsonResponse({'message': 'Faculty was deleted successfully!'}, status=status.HTTP_200_OK)

# Contribution REST API

@api_view(['GET', 'POST', 'DELETE'])
def contribution_list(request):
    if request.method == 'GET':
        contributions = Contribution.objects.all().order_by('id')

        title = request.query_params.get('title', None)
        if title is not None:
            contributions = contributions.filter(title__icontains=title)

        faculty = request.query_params.get('faculty',None)
        if faculty is not None:
            contributions = contributions.filter(faculty__id__icontains=faculty)

        contributions_serializer = ContributionSerializer(contributions, many=True)
        return JsonResponse(contributions_serializer.data, safe=False)

    elif request.method == 'POST':
        contribution_data = JSONParser().parse(request)
        contributions_serializer = ContributionSerializer(data=contribution_data)
        if contributions_serializer.is_valid():
            contributions_serializer.save()
            return JsonResponse(contributions_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(contributions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Contribution.objects.all().delete()
        return JsonResponse({'message': '{} Contributions were deleted successfully'.format(count[0])}, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def contribution_detail(request, pk):
    try:
        contribution = Contribution.objects.get(pk=pk)
    except Contribution.DoesNotExist:
        return JsonResponse({'message': 'The contribution does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        contribution_serializer = ContributionSerializer(contribution)
        return JsonResponse(contribution_serializer.data)

    elif request.method == 'PUT':
        contribution_data = JSONParser().parse(request)
        contribution_serializer = ContributionSerializer(contribution, data=contribution_data)
        if contribution_serializer.is_valid():
            contribution_serializer.save()
            return JsonResponse(contribution_serializer.data)
        return JsonResponse(contribution_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contribution.delete()
        return JsonResponse({'message': 'contribution was deleted successfully!'}, status=status.HTTP_200_OK)

# File Type REST API

@api_view(['GET', 'POST', 'DELETE'])
def filetype_list(request):
    if request.method == 'GET':
        filetypes = FileType.objects.all()

        title = request.query_params.get('type_name', None)
        if title is not None:
            filetypes = filetypes.filter(title_icontains=title)

        filetypes_serializer = FileTypeSerializer(filetypes, many=True)
        return JsonResponse(filetypes_serializer.data, safe=False)

    elif request.method == 'POST':
        filetype_data = JSONParser().parse(request)
        filetypes_serializer = FileTypeSerializer(data=filetype_data)
        if filetypes_serializer.is_valid():
            filetypes_serializer.save()
            return JsonResponse(filetypes_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(filetypes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = FileType.objects.all().delete()
        return JsonResponse({'message': '{} File types were deleted successfully'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def filetype_detail(request, pk):
    try:
        filetype = FileType.objects.get(pk=pk)
    except FileType.DoesNotExist:
        return JsonResponse({'message': 'The file type does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        filetype_serializer = FileTypeSerializer(filetype)
        return JsonResponse(filetype_serializer.data)

    elif request.method == 'PUT':
        filetype_data = JSONParser().parse(request)
        filetype_serializer = FileTypeSerializer(filetype, data=filetype_data)
        if filetype_serializer.is_valid():
            filetype_serializer.save()
            return JsonResponse(filetype_serializer.data)
        return JsonResponse(filetype_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        filetype.delete()
        return JsonResponse({'message': 'File type was deleted successfully!'}, status=status.HTTP_200_OK)

# User REST API

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        title = request.query_params.get('username', None)
        if title is not None:
            users = users.filter(username_icontains=title)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'This user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'This user was deleted successfully!'}, status=status.HTTP_200_OK)

#Send Email API
@api_view(['POST'])
def send_email(request):
    if request.method=='POST':
        receive_json_data = json.loads(request.body.decode('utf-8'))
        return StreamingHttpResponse('it was post request: ' + str(receive_json_data))
    return StreamingHttpResponse('it was GET request')

#Count vote API

@api_view(['POST'])
def up_vote(request,pk):
    try:
        contrib = Contribution.objects.get(pk = pk)
    except Contribution.DoesNotExist:
        return JsonResponse({'message': 'This contribution does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        contrib.vote += 1
        contrib.save()
        return JsonResponse({'message': 'Up vote successfully'}, status = status.HTTP_200_OK)

@api_view(['POST'])

def down_vote(request,pk):
    try:
        contrib = Contribution.objects.get(pk = pk)
    except Contribution.DoesNotExist:
        return JsonResponse({'message': 'This contribution does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        contrib.vote -= 1
        contrib.save()
        return JsonResponse({'message': 'Down vote successfully'}, status = status.HTTP_200_OK)

@api_view(['POST'])

def sign_in(request):
    receive_json_data = json.loads(request.body.decode('utf-8'))
    username = receive_json_data["username"]
    password = receive_json_data["password"]
    u = User.objects.filter(username= username,password=password)
    if not u:
        return JsonResponse({'check':'false'}, status=status.HTTP_200_OK)
    else:
        user = u.get()
        user_serialier = UserSerializer(user)
        return JsonResponse(user_serialier.data)

def get_all_file_paths(directory):
  
    file_paths = []
  
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    return file_paths  

@api_view(['GET'])

def download(request):
    firebase_storage = pyrebase.initialize_app(config)
    storage = firebase_storage.storage()

    dir = 'Home/static/tmp'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))

    list_path = Contribution.objects.filter(check_selected=True).values_list('note')
    for l in list_path:
        name = "".join(list_path[0])
        storage.child("downloads/" + name).download("Home/static/tmp/" + name)

    directory = './Home/static/tmp'
    file_paths = get_all_file_paths(directory)
    with ZipFile('download.zip','w') as zip:
        for file in file_paths:
            zip.write(file)
    storage.child("download.zip").put("download.zip")

    return JsonResponse({'message':'download success'},status=status.HTTP_204_NO_CONTENT)
