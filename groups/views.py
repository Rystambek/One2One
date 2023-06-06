from django.http import HttpRequest, JsonResponse
from .models import Group
from users.models import User, Contact
from users.views import to_dict


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
    

