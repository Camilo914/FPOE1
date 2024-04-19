from django.db import models
class Celular(models.Model):
	Modelo 				= models.TextField()
	Cuantas_Gb_Ram 		= models.TextField()
	Tipo_pantalla 		= models.TextField()
	Nombre_Procesador	= models.TextField()
	
	def __str__(self):
		return self.Modelo