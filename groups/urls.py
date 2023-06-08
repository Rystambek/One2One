from django.urls import path
from .views import (
    get_groups,
    get_groups_id,
    group_id_all_students,
    remove
)
                     
urlpatterns = [
    path('', get_groups),
    path('<int:id>',get_groups_id),
    path('<int:id>/students',group_id_all_students),
    path('<int:group_id>/remove/<int:id>',remove)

]
