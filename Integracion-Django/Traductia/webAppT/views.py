# Importanciones para el uso de JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from webAppT import views
from .models import Usuario, Rango, Sector
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Count

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# Importanciones de la libreria openai para el uso de la IA traductora
import os
import ffmpeg
import openai
import subprocess
from django import forms

API_KEY = "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"
media_file_path = "../Traductia/audios/temp/temp_blob.wav"
media_file = open(media_file_path, "rb")
model_id = "whisper-1"


# --trabajo para español-----------------------------------
@csrf_exempt
def whisper_ES(request):
    if request.method == "POST":
        audio_blob_list = request.FILES.getlist("music")
        if len(audio_blob_list) > 0:
            audio_blob = audio_blob_list[0]  # Tomar el primer archivo de la lista
            print("dentro")
            print(audio_blob.name)

        temp_file_path = "../Traductia/audios/temp/temp_blob.wav"
        with open(temp_file_path, "wb") as temp_file:
            for chunk in audio_blob.chunks():
                temp_file.write(chunk)

        media_file = open("../Traductia/audios/temp/temp_blob.wav", "rb")
        transcript = openai.Audio.transcribe(
            api_key=API_KEY, model=model_id, file=media_file, response_format="text"
        )
        print(transcript)
        media_file = open("../Traductia/audios/temp/temp_blob.wav", "rb")
        translate = openai.Audio.transcribe(
            api_key=API_KEY,
            model=model_id,
            file=media_file,
            response_format="text",
            language="es",
        )
        print(translate)
    return JsonResponse({"transcript": transcript, "translate": translate})


# --trabajo para haitiano-----------------------------------
@csrf_exempt
def whisper_HT(request):
    if request.method == "POST":
        audio_blob_list = request.FILES.getlist("music")
        if len(audio_blob_list) > 0:
            audio_blob = audio_blob_list[0]  # Tomar el primer archivo de la lista
            print("dentro")
            print(audio_blob.name)

        temp_file_path = "../Traductia/audios/temp/temp_blob.wav"
        with open(temp_file_path, "wb") as temp_file:
            for chunk in audio_blob.chunks():
                temp_file.write(chunk)

        media_file = open("../Traductia/audios/temp/temp_blob.wav", "rb")
        transcript = openai.Audio.transcribe(
            api_key=API_KEY, model=model_id, file=media_file, response_format="text"
        )
        print(transcript)
        media_file = open("../Traductia/audios/temp/temp_blob.wav", "rb")
        translate = openai.Audio.transcribe(
            api_key=API_KEY,
            model=model_id,
            file=media_file,
            response_format="text",
            language="ht",
        )
        print(translate)
    return JsonResponse({"transcript": transcript, "translate": translate})


# ----------------------------------------------------------
# -----------Trabajo de audio-------------------------------
@csrf_exempt
def upload_audio(request):
    if request.method == "POST":
        audio_blob_list = request.FILES.getlist("music")
        if len(audio_blob_list) > 0:
            audio_blob = audio_blob_list[0]  # Tomar el primer archivo de la lista
            print("dentro")
            print(audio_blob.name)

        temp_file_path = "../Traductia/audios/temp/temp_blob.wav"
        with open(temp_file_path, "wb") as temp_file:
            for chunk in audio_blob.chunks():
                temp_file.write(chunk)

        media_file = open("../Traductia/audios/temp/temp_blob.wav", "rb")
        transcript = openai.Audio.transcribe(
            api_key=API_KEY, model=model_id, file=media_file, response_format="text"
        )
        print(transcript)
        media_file = open("../Traductia/audios/temp/temp_blob.wav", "rb")
        translate = openai.Audio.translate(
            api_key=API_KEY, model=model_id, file=media_file, response_format="text"
        )
        print(translate)
    return JsonResponse({"transcript": transcript, "translate": translate})


# ----------------------------------------------------------
@login_required
def index(request):
    # Obtener los datos de la base de datos
    usuarios = Usuario.objects.all()
    rango = Rango.objects.all()
    sector = Sector.objects.all()

    administrativos = Usuario.objects.filter(sector_id=1).count
    funcionarios = Usuario.objects.filter(sector_id=2).count
    publicos = Usuario.objects.filter(sector_id=3).count

    # Pasar los datos del contexto al template
    context = {
        "usuarios": usuarios,
        "rango": rango,
        "sector": sector,
        "administrativos": administrativos,
        "funcionarios": funcionarios,
        "publicos": publicos,
    }

    return render(request, "index.html", context)


# definiciones de sesion
def login(request):
    return render(request, "registration/login.html")


def exit(request):
    logout(request)
    return redirect("index")


@login_required
def perfilConectado(request):
    return redirect(index.html)


# definiciones para el traductor
@login_required
def traductorIA(request):
    # debo declarar los atributos para poder llamar  alos sectores, ademas debo contar la accion del click del boton
    sector = Sector.objects.all()
    data = {"sector": sector}
    return render(request, "traductor.html", data)


# metodo para  ver Lista usuarios
@login_required
def vistaPerfil(request):
    usuarios = Usuario.objects.all()  # trae todo
    rango = Rango.objects.all()
    sector = Sector.objects.all()

    nombre_busqueda = request.GET.get("nombre_busqueda")
    if nombre_busqueda:
        usuarios = usuarios.filter(nombreUsuario__icontains=nombre_busqueda)

    data = {
        "usuario": usuarios,
        "rango": rango,
        "sector": sector,
        "nombre_busqueda": nombre_busqueda,
    }
    return render(request, "perfilAdmin.html", data)


# metodo para ingresar datos al formulario de ingresar usuario
@login_required
def ingresar(request):
    rango = Rango.objects.all()
    sector = Sector.objects.all()
    data = {"rango": rango, "sector": sector}
    return render(request, "perfilAdminIngresar.html", data)


# metodo para agregar usuarios(push)
def agregar(request):
    rutUsuario = request.POST["rutUsuario"]
    nombreUsuario = request.POST["nombreUsuario"]
    apellidosUsuario = request.POST["apellidosUsuario"]
    sector = request.POST["sector"]
    rango = request.POST["rango"]
    user = request.POST["user"]
    password = request.POST["password"]

    usuario = Usuario.objects.create(
        rutUsuario=rutUsuario,
        nombreUsuario=nombreUsuario,
        apellidosUsuario=apellidosUsuario,
        sector_id=sector,
        rango_id=rango,
        user=user,
        password=password,
    )
    return redirect("/usuarios/")


# metodo para eliminar usuarios
def eliminar(request, id):
    usuarios = Usuario.objects.get(id=id)
    usuarios.delete()
    return redirect("/usuarios/")


# metodo para ver datos a editar
def editar(request, id):
    usuarios = Usuario.objects.get(id=id)
    rango = Rango.objects.all()
    sector = Sector.objects.all()
    data = {
        "titulo": "Edicion de Usuarios",
        "usuario": usuarios,
        "rango": rango,
        "sector": sector,
    }

    return render(request, "editarUsuario.html", data)


# metodo para editar datos
def editarUsuario(request):
    rango = Rango.objects.all()
    sector = Sector.objects.all()

    id = request.POST["id"]
    rutUsuario = request.POST["rutUsuario"]
    nombreUsuario = request.POST["nombreUsuario"]
    apellidosUsuario = request.POST["apellidosUsuario"]
    sector = request.POST["sector"]
    rango = request.POST["rango"]
    user = request.POST["user"]
    password = request.POST["password"]

    usuario = Usuario.objects.get(id=id)
    usuario.rutUsuario = rutUsuario
    usuario.nombreUsuario = nombreUsuario
    usuario.apellidosUsuario = apellidosUsuario
    usuario.sector_id = sector
    usuario.rango_id = rango
    usuario.user = user
    usuario.password = password

    usuario.save()

    return redirect("/usuarios/")


# aumentador de usos por boton
def aumentar_usos(request):
    if request.method == "POST":
        sector_id = request.POST.get("sector_id")
        sector = get_object_or_404(Sector, id=sector_id)
        # Realiza las actualizaciones necesarias en la base de datos para aumentar los usos del sector
        sector.usos += 1
        sector.save()
        return redirect(
            "/"
        )  # Redirige a la página deseada después de aumentar los usos
    else:
        return redirect(
            "/usuarios/"
        )  # Redirige a la página deseada si la solicitud no es POST
