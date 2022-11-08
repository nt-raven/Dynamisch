
from django.urls import path, include
from . import views

# urlpatterns = [
#     path("", views.index_view, name="index"),
# ]
# urlpatterns = [
#     path("", views.index_form, name="index"),
# ]

urlpatterns = [
    path("", views.insert_page, name="insert_page"),
    path("index/", views.insert_data, name="index"),
    path("show_page/", views.show_page, name="show_page"),
    path("update_page/<int:pk>", views.update_page, name="update_page"),
    path("update_data/<int:pk>", views.update_data, name="update_data"),
    path("delete_data/<int:pk>", views.delete_data, name="delete_data"),
]