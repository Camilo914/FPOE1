from django.db import models
class Celular(models.Model):
	Modelo 				= models.CharField(max_length=50)
	Cuantas_Gb_Ram 		= models.TextField()
	Tipo_pantalla 		= models.TextField()
	Nombre_Procesador	= models.TextField()
	
	def __str__(self):
		return self.title