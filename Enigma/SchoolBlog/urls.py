from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ActualizarComunicado, CrearComunicado, home, listar_comunicados, filtrar_comunicados, comunicado_list

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', home, name='home'),
    path('listar/', listar_comunicados, name='listar_comunicados'),
    path('filtrar/', filtrar_comunicados, name='filtrar_comunicados'),
    path('crear/', CrearComunicado.as_view(), name='crear_comunicados'),
    path('actualizar/<pk>', ActualizarComunicado.as_view(), name='actualizar_comunicados'),
    path('comunicados/', comunicado_list, name='comunicado_list'),
]