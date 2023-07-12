from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from Oncoliq.models import *
from Oncoliq.forms import *

@login_required
def inicio(request):
    return render (request,"Oncoliq/inicio.html")

@login_required
def laboratorio(request):
    laboratorio = Laboratorio.objects.all()
    return render (request,"Oncoliq/laboratorio/laboratorio.html", {"Laboratorio": laboratorio})

@login_required
def medico(request):
    medico = Medico.objects.all()
    return render (request, "Oncoliq/medico/medico.html", {"Medico":medico})

@login_required
def paciente(request):
    paciente = Paciente.objects.all()
    return render (request, "Oncoliq/paciente/paciente.html", {"Paciente":paciente})

@login_required
def setLaboratorio(request):
    if request.method == 'POST':
        miFormulario = formSetLaboratorio(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            laboratorio = Laboratorio(laboratorio=data["laboratorio"],operario=data["operario"],email=data["email"],equipo=data["equipo"],fecha=data["fecha"],resultado=data["resultado"])
            laboratorio.save()
            return render(request,"Oncoliq/inicio.html")
    else:
        miFormulario = formSetLaboratorio()

    return render(request,"Oncoliq/laboratorio/setLaboratorio.html",{"miFormulario":miFormulario})

@login_required
def getLaboratorio(request):
    return render (request, "Oncoliq/laboratorio/getLaboratorio.html")

@login_required
def buscarLaboratorio(request):
    if request.GET["operario"]:
        operario = request.GET["operario"]
        operario = Laboratorio.objects.filter(operario = operario)
        return render(request,"Oncoliq/laboratorio/getLaboratorio.html",{"operario":operario})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

@login_required
def setMedico(request):
    if request.method == 'POST':
        miForm = formSetMedico(request.POST)
        print(miForm)
        if miForm.is_valid:
            data2 = miForm.cleaned_data
            medico = Medico(nombre=data2["nombre"],apellido=data2["apellido"],email=data2["email"],institucion=data2["institucion"],informe=data2["informe"],mamografia=data2["mamografia"])
            medico.save()
            return render(request,"Oncoliq/inicio.html")
    else:
        miForm = formSetMedico()

    return render(request,"Oncoliq/medico/setMedico.html",{"miForm":miForm})

@login_required
def getMedico(request):
    return render (request, "Oncoliq/medico/getMedico.html")

@login_required
def buscarMedico(request):
    if request.GET["email"]:
        email = request.GET["email"]
        email = Medico.objects.filter(email = email)
        return render(request,"Oncoliq/medico/getMedico.html",{"email":email})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

@login_required
def setPaciente(request):
    if request.method == 'POST':
        miForm2 = formSetPaciente(request.POST)
        print(miForm2)
        if miForm2.is_valid:
            data3 = miForm2.cleaned_data
            paciente = Paciente(nombre=data3["nombre"],apellido=data3["apellido"],email=data3["email"])
            paciente.save()
            return render(request,"Oncoliq/inicio.html")
    else:
        miForm2 = formSetPaciente()

    return render(request,"Oncoliq/paciente/setPaciente.html",{"miForm2":miForm2})

@login_required
def getPaciente(request):
    return render (request, "Oncoliq/paciente/getPaciente.html")

@login_required
def buscarPaciente(request):
    if request.GET["email"]:
        email = request.GET["email"]
        email = Paciente.objects.filter(email = email)
        return render(request,"Oncoliq/paciente/getPaciente.html",{"email":email})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

@login_required
def eliminarLaboratorio(request, nombre_laboratorio):
    laboratorio = Laboratorio.objects.get(laboratorio=nombre_laboratorio)
    laboratorio.delete()
    miFormulario = formSetLaboratorio()
    laboratorios = Laboratorio.objects.all()
    return render(request,"Oncoliq/laboratorio/laboratorio.html",{"miFormulario":miFormulario,"laboratorios":laboratorios})

@login_required
def editarLaboratorio(request, nombre_laboratorio):
    laboratorio = Laboratorio.objects.get(laboratorio= nombre_laboratorio)
    if request.method == 'POST':
        
        miFormulario = formSetLaboratorio(request.POST)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data

            laboratorio.laboratorio = data['laboratorio']
            laboratorio.operario = data['operario']
            laboratorio.email = data['email']
            laboratorio.equipo = data['equipo']
            laboratorio.fecha = data['fecha']
            laboratorio.resultado = data['resultado']
            laboratorio.save()
            miFormulario = formSetLaboratorio()
            laboratorios = Laboratorio.objects.all()
            return render(request,"Oncoliq/setLaboratorio.html",{"miFormulario":miFormulario,"laboratorios":laboratorios})
    else:
        miFormulario = formSetLaboratorio(initial={'laboratorio': laboratorio.laboratorio, 'operario': laboratorio.operario, 'email': laboratorio.email, 'equipo': laboratorio.equipo, 'fecha': laboratorio.fecha, 'resultado': laboratorio.resultado})
    return render(request,"Oncoliq/laboratorio/editarLaboratorio.html",{"miFormulario":miFormulario})

@login_required
def eliminarMedico(request, nombre_medico):
    medico = Medico.objects.get(nombre=nombre_medico)
    medico.delete()
    miFormulario = formSetMedico()
    medicos = Medico.objects.all()
    return render(request,"Oncoliq/medico/medico.html",{"miFormulario":miFormulario,"medicos":medicos})

@login_required
def editarMedico(request, nombre_medico):
    medico = Medico.objects.get(nombre= nombre_medico)
    if request.method == 'POST':
        
        miFormulario = formSetMedico(request.POST)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data

            medico.nombre = data['nombre']
            medico.apellido = data['apellido']
            medico.email = data['email']
            medico.institucion = data['institucion']
            medico.informe = data['informe']
            medico.mamografia = data['mamografia']
            medico.save()
            miFormulario = formSetMedico()
            medicos = Medico.objects.all()
            return render(request,"Oncoliq/setMedico.html",{"miFormulario":miFormulario,"medicos":medicos})
    else:
        miFormulario = formSetMedico(initial={'nombre': medico.nombre, 'apellido': medico.apellido, 'email': medico.email, 'institucion': medico.institucion, 'informe': medico.informe, 'mamografia': medico.mamografia})
    return render(request,"Oncoliq/medico/editarMedico.html",{"miFormulario":miFormulario})

@login_required
def eliminarPaciente(request, nombre_paciente):
    paciente = Paciente.objects.get(nombre=nombre_paciente)
    paciente.delete()
    miFormulario = formSetPaciente()
    pacientes = Paciente.objects.all()
    return render(request,"Oncoliq/paciente/paciente.html",{"miFormulario":miFormulario,"pacientes":pacientes})

@login_required
def editarPaciente(request, nombre_paciente):
    paciente = Paciente.objects.get(nombre= nombre_paciente)
    if request.method == 'POST':
        
        miFormulario = formSetPaciente(request.POST)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data

            paciente.nombre = data['nombre']
            paciente.apellido = data['apellido']
            paciente.email = data['email']
            paciente.save()
            miFormulario = formSetPaciente()
            pacientes = Paciente.objects.all()
            return render(request,"Oncoliq/setPaciente.html",{"miFormulario":miFormulario,"pacientes":pacientes})
    else:
        miFormulario = formSetPaciente(initial={'nombre': paciente.nombre, 'apellido': paciente.apellido, 'email': paciente.email})
    return render(request,"Oncoliq/paciente/editarPaciente.html",{"miFormulario":miFormulario})

def loginWeb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'Oncoliq/inicio.html')
        else:
            return render(request, 'Oncoliq/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'Oncoliq/login.html')
    
def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, 'Oncoliq/login.html')
    else:
        return render(request, 'Oncoliq/registro.html')
    
@login_required    
def perfilview(request):
    return render(request, 'Oncoliq/Perfil/perfil.html')

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'Oncoliq/Perfil/perfil.html')
    else:
        form = UserEditForm(initial={'username':usuario.username, 'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name})
        return render(request, 'Oncoliq/Perfil/editarPerfil.html', {"form":form})

@login_required   
def changePassword(request):
    usuario = request.user
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse("Las contraseñas no coinciden")
        return render(request, 'Oncoliq/inicio.html')
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, 'Oncoliq/Perfil/changePassword.html', {"form":form})
    
@login_required
def editAvatar(request):
    if request.method == 'POST':
        form = avatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'Oncoliq/inicio.html', {'avatar':avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = avatarForm()
        except:
            form = avatarForm()
    return render(request, 'agregarAvatar.html', {'form':form})

def getAvatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar