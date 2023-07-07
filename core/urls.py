from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", home, name="home"),    
    path("login", LoginView.as_view(template_name="core/login.html"), name="login"),    
    path("logout", logout, name="logout"),
    path("registro", registro, name="registro"),
    path("seguimiento", seguimiento, name="seguimiento"),
    path("compras", compras, name="compras"),
    path("productos", productos, name="productos"),  
    path("plantas", plantas, name="plantas"),  
    path("cactus", cactus, name="cactus"),
    path("suculentas", suculentas, name="suculentas"),
    path("maceteros", maceteros, name="maceteros"),
    path("decoracion", decoracion, name="decoracion"),
    path("sustratos", sustratos, name="sustratos"),
    path("utensilios", utensilios, name="utensilios"),
    path("registro", registro, name="registro"),
    path("carrito", carrito, name="carrito"),
    path("comprar", comprar, name="comprar"),
    path("limpiar", limpiar, name="limpiar"),
    path("historial", historial, name="historial"),
    path("suscribir", suscribir, name="suscribir"),
    path("detalle/<int:id>", detalle, name="detalle"),
    path("addtocar/<codigo>", addtocar, name="addtocar"),
    path("droptocar/<codigo>", droptocar, name="droptocar")
]