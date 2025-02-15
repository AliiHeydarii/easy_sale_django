from django.urls import path
from . import views

urlpatterns = [
    path('' , views.IndexView.as_view() , name='index'),
    path('ad-detail/<int:pk>',views.AdDetailView.as_view(),name='ad-detail'),
    path('ad-create/' , views.AdCreateFormView.as_view(),name='ad-create'),
    path('ad-category/<str:name>/' , views.AdCategoryView.as_view(),name='ad-category')
]