from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('create', BlogCreateView.as_view()),
    path('list/', BlogListView.as_view()),
    path('detail/<int:pk>/', BlogDetailView.as_view()),
]