from django.contrib import admin
from django.urls import path, include
from webAppT import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # verificador de sesion
    path("accounts/", include("django.contrib.auth.urls")),

    #path que toma la accion del boton para simular la sesion de tipos de usuarios
    path("aumentar_usos/", views.aumentar_usos, name="aumentar_usos"),

    # pagina inicio
    path("", views.index, name="index"),

    # login (no lo entiendo # ma o meno)
    path("/", views.perfilConectado, name="login"),

    # perfiles de usuario urls de CRUD
    path("usuarios/", views.vistaPerfil, name="listaUsuarios"),
    path("perfilAdminIngresar.html", views.ingresar),
    path("addUsuario/", views.agregar),
    path("eliminar/<int:id>", views.eliminar),
    path("modificar/<int:id>", views.editar),
    path("editarUsuario/", views.editarUsuario),

    # urls asociadas al template del Traductor
    path("traductor/", views.traductorIA, name="traductor"),
    path("json/", views.whisper_ES, name="whisper_transcript"),
    path("jsont/", views.whisper_HT, name="whisper_translate"),
    path('upload/', views.upload_audio, name='upload_audio'),
]
