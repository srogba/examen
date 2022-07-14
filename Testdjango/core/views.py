from django.shortcuts import get_object_or_404, render, redirect
from .models import Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario



    return render(request, 'core/contacto.html', data)

def galeria(request):
    return render(request, 'core/galeria.html')

@permission_required('core.add_producto')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario    
    
    return render(request, 'core/producto/agregar.html', data)

@permission_required('core.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }


    return render(request, 'core/producto/listar.html', data)

@permission_required('core.change_producto')
def modificar_producto(request, codigo):
    
    producto = get_object_or_404(Producto, codigo=codigo)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
            data["form"] = formulario
     

    return render(request,'core/producto/modificar.html', data)

@permission_required('core.delete_producto')
def eliminar_producto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
        
    return render(request, 'registration/registro.html', data)
  
