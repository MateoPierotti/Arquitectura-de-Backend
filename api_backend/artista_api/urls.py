
from django.urls import path
from artista_api import views
from .views import ArtistaListView

urlpatterns = [

    # path('index_artista/', views.index_artista, name='index_artista'),
    path('new_artista/', views.NewArtistaView.as_view(), name='new_artista'),
    path('artista_rest/', views.artista_rest, name='artista_rest'),
    path('artista_list/', ArtistaListView.as_view(), name='artista_list'),



    path('home_canciones/', views.home_canciones, name='home_canciones'),
    path('new_cancion/', views.NewCancionView.as_view(), name='new_cancion'),
    path('cancion_rest/', views.cancion_rest, name='cancion_rest'),

    

    ]