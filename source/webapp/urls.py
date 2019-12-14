from django.urls import path
from webapp.views import IndexView, PhotoView, AddPhoto

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_detail'),
    path('photo/add/', AddPhoto.as_view(), name='add_photo')
]
