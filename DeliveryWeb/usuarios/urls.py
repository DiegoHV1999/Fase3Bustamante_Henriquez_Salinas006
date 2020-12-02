from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('sobrenosotros/', views.sobrenosotros, name='sobrenosotros'),
    path('local/<int:pk>/', views.LocalDetailView.as_view(), name='local_detail'),
    path('local/', views.LocalListView.as_view(), name='locales'),
    path('transporte/<uuid:pk>/', views.transporteDetailView.as_view(), name='transporte_detail'),
    path('transporte/', views.transporteListView.as_view(), name='transportes'),
    


]

urlpatterns+=[
    path('local/create/', views.LocalCreate.as_view(), name='local_create'),
    path('local/<int:pk>/update/', views.LocalUpdate.as_view(), name='local_update'),
    path('local/<int:pk>/delete/', views.LocalDelete.as_view(), name='local_delete'),
    path('transporte/create/', views.transporteCreate.as_view(), name='transporte_create'),
    path('transporte/<uuid:pk>/update/',views.transporteUpdate.as_view(), name='transporte_update'),
    path('transporte/<uuid:pk>/delete/', views.transporteDelete.as_view(), name='transporte_delete'),
    
    
]