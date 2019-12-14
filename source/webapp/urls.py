from django.urls import path
from webapp.views import IndexView, PhotoView, AddPhoto, EditPhoto, DeletePhoto

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_detail'),
    path('photo/add/', AddPhoto.as_view(), name='add_photo'),
    path('photo/<int:pk>/edit/', EditPhoto.as_view(), name='edit_photo'),
    path('photo/<int:pk>/delete/', DeletePhoto.as_view(), name='delete_photo'),
]
