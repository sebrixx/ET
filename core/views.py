from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
import requests

def home(request):
    plantas = Producto.objects.filter(categoria=Categoria.objects.get(nombre="Plantas"))
    context = {'plantas' :plantas}
    suscrito(request, context)
    print(context)
    return render(request, 'core/index.html', context)

def suscribir(request):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)
    else:
        suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]

def seguimiento(request):
    return render(request, 'core/seguimiento.html')

def compras(request):
    return render(request, 'core/historial_compras.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/plantas.html',{"plantas":plantas, "carro":request.session.get("carro",[])})
    
def plantas(request):
    plantas = Producto.objects.filter(categoria=Categoria.objects.get(nombre="Plantas"))
    return render(request, 'core/carrito.html', {"plantas":plantas, "carro":request.session.get("carro", [])})

def cactus(request):
    cactus = Producto.objects.filter(categoria=Categoria.objects.get(nombre="Cactus"))
    return render(request, 'core/cactus.html', {"cactus":cactus, "carro":request.session.get("carro", [])})

def suculentas(request):
    suculentas = Producto.objects.filter(categoria=Categoria.objects.get(nombre="Suculentas"))
    return render(request, 'core/suculentas.html', {"suculentas":suculentas, "carro":request.session.get("carro", [])})

def maceteros(request):
    maceteros = Producto.objects.filter(categoria=Categoria.objects.get(nombre="Maceteros"))
    return render(request, 'core/maceteros.html', {"maceteros":maceteros, "carro":request.session.get("carro", [])})

def decoracion(request):
    decoracion = Producto.objects.filter(categoria=Categoria.objects.get(nombre="Decoración"))
    return render(request, 'core/decoracion.html', {"decoracion":decoracion, "carro":request.session.get("carro", [])})

def sustratos(request):
    sustratos = Producto.objects.filter(categoria=Categoria.objects.get(nombre="Sustratos"))
    return render(request, 'core/sustratos.html', {"sustratos":sustratos, "carro":request.session.get("carro", [])})

def utensilios(request):
    utensilios = Producto.objects.filter(categoria=Categoria.objects.get(nombre="Utensilios"))
    return render(request, 'core/utensilios.html', {"utensilios":utensilios, "carro":request.session.get("carro", [])})

def login(request):
    return render(request, 'core/login.html')

def logout(request):
    return logout_then_login(request, login_url="login")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:        
        registro = Registro()
    return render(request, 'core/registro.html', {'form':registro})

def addtocar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
        carro.append([codigo, producto.nombre, producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="productos")

def droptocar(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")

def limpiar(request):
    request.session.flush()
    return redirect(to="productos")

def carrito(request):
    return render(request, 'core/carrito.html', {"carro":request.session.get("carro", [])})

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        request.session["carro"] = []
        
        producto = Producto.objects.get(codigo = item[0])
        producto.stock -= item[4]
        producto.save()
        request.session["carro"] = []
    return redirect(to="carrito")

def historial(request):
    if request.user.is_authenticated:
        redirect(to="login")
    compras = Venta.objects.filter(cliente=request.user)
    return render(request, 'core/historial.html', {'compras':compras})

def detalle(request, id):
    try:
        venta = Venta.objects.get(id=id)
        detalle = DetalleVenta.objects.filter(venta=venta)
    except Venta.DoesNotExist:
        detalle = None
    return render(request, "core/detalle.html", {"detalle": detalle})