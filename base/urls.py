from django.urls import path
from . import views

# name can specific path in the later
urlpatterns = [
    path('register/',views.register_user, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    path('create-room/', views.create_room,name="create-room"),
    path('update-room/<str:pk>', views.updated_room, name="update-room"),
    path('delete-room/<str:pk>', views.delete_room,name="delete-room")

    # parsing the params <str:pk>
]