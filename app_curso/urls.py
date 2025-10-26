from django.urls import path
from . import views

app_name = 'app_curso'

urlpatterns = [
    path('', views.listar_cursos, name='listar_cursos'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('crear/', views.crear_curso, name='crear_curso'),
    path('editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('borrar/<int:curso_id>/', views.borrar_curso, name='borrar_curso'),
    path('curso/<int:curso_id>/material/crear/', views.crear_material, name='crear_material'),
]