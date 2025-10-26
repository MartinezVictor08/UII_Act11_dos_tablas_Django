from django.db import models

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField()
    duracion_semanas = models.IntegerField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    estudiantes = models.IntegerField()
    foto = models.ImageField(upload_to='cursos', null=True, blank=True)

    def __str__(self):
        return self.nombre_curso

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['nombre_curso']


class Material(models.Model):
    nombre_material = models.CharField(max_length=150)
    tipo_material = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    costo_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    en_stock = models.IntegerField()
    
    # Relación Foránea
    id_curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE, 
        related_name='materiales_requeridos',
        db_column='id_curso' 
    )

    def __str__(self):
        return f"{self.nombre_material} ({self.tipo_material}) para {self.id_curso.nombre_curso}"

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
        unique_together = ('nombre_material', 'id_curso')