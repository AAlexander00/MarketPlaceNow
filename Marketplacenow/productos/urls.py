from django.urls import path
from . import views

urlpatterns = [
    path('busqueda/', views.busqueda, name='busqueda'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('', views.lista_productos, name='inicio'),
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('<int:producto_id>/tallas/', views.obtener_tallas, name='obtener_tallas'),
    path('<int:producto_id>/colores/', views.obtener_colores, name='obtener_colores'),
    path('nuevo/', views.crear_producto, name='crear_producto'),  # ✅ Ruta protegida
    path('ofertas/', views.ofertas, name='ofertas'),  # ✅ Ruta protegida
    path('nuevo_productos/', views.nuevo, name='nuevo'),  # ✅ Ruta protegida
    path('telefono/', views.telefono, name='telefono'),
    path('computador/', views.computador, name='computador'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('hombres/', views.hombres, name='hombres'),
    path('mujeres/', views.mujeres, name='mujeres'),
    path('ninos/', views.ninos, name='ninos'),
    path('joyas/', views.joyas, name='joyas'),
    path('calzado/', views.calzado, name='calzado'),
    path('muebles/', views.muebles, name='muebles'),
    path('exterior/', views.exterior, name='exterior'),
    path('interior/', views.interior, name='interior'),
    path('decoracion/', views.decoracion, name='decoracion'),
    path('jardineria/', views.jardineria, name='jardineria'),
    path('ficcion/', views.ficcion, name='ficcion'),
    path('romance/', views.romance, name='romance'),
    path('infantiles/', views.infantiles, name='infantiles'),
    path('favoritos/', views.ver_favoritos, name='favoritos'),
    path('toggle-favorito/<int:producto_id>/', views.toggle_favorito, name='toggle_favorito'),
]
