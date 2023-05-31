from django.urls import path
from .views import (
    get_users,
    get_user_id,
    contact
)
                     

urlpatterns = [
    path('/', get_users),
    path('/<int:id>',get_user_id),
    path('/<int:id>/contact/',contact)
]
