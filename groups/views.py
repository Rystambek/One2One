from django.http import HttpRequest, JsonResponse
from .models import Group
from django.core.exceptions import ObjectDoesNotExist
from users.models import User, Contact
from users.views import to_dict
import json


def to_dict_group(group):
    return {
        "id": group.id,
        "name": group.name,
        "students": [to_dict(student) for student in group.students.all()]
    }


def get_groups(request):
    if request.method == "GET":
        groups = Group.objects.all()
        group_list = [to_dict_group(group) for group in groups]
        return JsonResponse(group_list, safe=False)
    
    elif request.method == 'POST':
        data_json = request.body.decode()
        data = json.loads(data_json)

        if not data.get('name'):
            return JsonResponse({'status':"name yo'q"})

        group = Group.objects.create(
            name = data['name']
        )

        group.save()

        return JsonResponse(to_dict_group(group))
    
def get_groups_id(request:HttpRequest,id) -> JsonResponse:
    if request.method == "GET":
        try:
            group = Group.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        
        return JsonResponse(to_dict_group(group))
    
    elif request.method == "PUT":
        try:
            group = Group.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('name'):
            group.name = data['name']

        group.save()

        return JsonResponse(to_dict_group(group))
    
    elif request.method == "DELETE":
        try:
            group = Group.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        group.delete()

        return JsonResponse({'status': 'ok'})

def group_id_all_students(request:HttpRequest,id) -> JsonResponse:
    if request.method == 'GET':
        try:
            group = Group.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        students = to_dict_group(group)['students']
        return JsonResponse(students,safe=False)

def remove(request:HttpRequest,group_id,id) -> JsonResponse:
    if request.method == 'DELETE':
        try:
            student = User.objects.get(id = id)
            group = Group.objects.filter(id = group_id,students=student)
            
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
            
        group.delete()
        return JsonResponse({"status":200})