from django.contrib import admin
from django.urls import path,include #importamos include tambien
from . import views

urlpatterns = [
    # Configuración de la administración de Django
    path('admin/', admin.site.urls),

    # URLs de autenticación de Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Incluye las URLs de la aplicación 'pages'
    #path('', include('pages.urls')),

    # Resto de las URLs definidas en el proyecto principal
    path('', views.index_page, name='index-page'),
    path('login/', views.index_page, name='login'),
    path('home/', views.home, name='home'),

    path('buscar/', views.search, name='buscar'),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path('exit/', views.exit, name='exit'),
    path('salir/',views.salir,name='salir'),
    
] 
