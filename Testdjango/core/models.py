from django.db import models

# Create your models here.
class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True, verbose_name= 'Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name= 'Nombre de la categoria')
    

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name= 'id_sku')
    nombre = models.CharField(max_length=50, verbose_name= 'Nombre Producto')
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.PROTECT)
    fecha_pedido = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.codigo
  
opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]

]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

