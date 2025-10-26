from django import forms
from .models import Curso, Material

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'descripcion', 'duracion_semanas', 'costo', 'estudiantes', 'foto']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre_material', 'tipo_material', 'proveedor', 'costo_unitario', 'en_stock']