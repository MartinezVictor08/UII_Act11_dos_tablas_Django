from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'detalle_curso.html', {'curso': curso})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # CORREGIDO: Usar el nombre completo 'app_curso:listar_cursos'
            return redirect('app_curso:listar_cursos') 
    else:
        form = CursoForm()
    return render(request, 'formulario_curso.html', {'form': form, 'titulo': 'Crear Curso'})

def editar_curso(request, curso_id):
    # Obtiene el curso o devuelve un 404
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso) 
        if form.is_valid():
            form.save()
         
            return redirect('app_curso:detalle_curso', curso_id=curso.id) 
    else:
        form = CursoForm(instance=curso)

    return render(request, 'formulario_curso.html', {'form': form, 'titulo': 'Editar Curso'})

def borrar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        curso.delete()
        # Asume el nombre de URL 'listar_cursos'
        return redirect('app_curso:listar_cursos') 
    return render(request, 'confirmar_borrar.html', {'curso': curso})

def crear_material(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = MaterialForm(request.POST) 
        if form.is_valid():
            material = form.save(commit=False)
            material.id_curso = curso
            material.save()
            return redirect('app_curso:detalle_curso', curso_id=curso.id) 
    else:
        form = MaterialForm() 

    return render(request, 'formulario_material.html', {
        'form': form,
        'titulo': f'Agregar Material para {curso.nombre_curso}'
    })