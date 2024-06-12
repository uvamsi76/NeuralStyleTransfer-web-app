from django.urls import path
from .views import ImageProcessView

urlpatterns = [
    path('process-image/', ImageProcessView.as_view(), name='process-image'),
]
