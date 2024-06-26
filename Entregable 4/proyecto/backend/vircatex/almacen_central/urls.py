from django.urls import path
from . import views
from .views import LotesEntreFechasView, ProveedorMateriaPrimaView, CrearProveedorView

urlpatterns = [
    path('almacen_central/lotes/', views.LoteListView.as_view(), name='lote-list'),
    path('almacen_central/lotes_entre_fechas/', LotesEntreFechasView.as_view()),
    path('almacen_central/proveedor_materia_prima/', ProveedorMateriaPrimaView.as_view()),
    path('almacen_central/lote_entrada/', views.LotesEntradaView.as_view()),
    path('almacen_central/lote_salida/', views.LotesSalidaView.as_view()),
    path('almacen_central/crear_proveedor/', CrearProveedorView.as_view()),
]