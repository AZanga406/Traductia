from django.utils import timezone
from django.db import models

# Create your models here(CLASES DE LA BASE DE DATOS).

#Clase que contiene el rango del usuario en la base de datos
class Rango(models.Model):
    nombreRango = models.CharField(max_length=100,verbose_name='Rango del Funcionario')
    creado = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return '{}'.format(self.nombreRango)
    
#Clase que contiene el sector al cual pertenece el usuario en la base de datos
class Sector(models.Model):    
    nombreDepartamento = models.CharField(max_length=100,verbose_name='Nombre del Departamento')
    usos = models.SmallIntegerField(max_length=9000, verbose_name='Cantidad de Usos', default=0)
    def _str_(self):
        return '{}'.format(self.nombreDepartamento)
    
    class Meta:
        verbose_name='Sector'  #como se muestra en tabla
        verbose_name_plural='Sectores'  #como se mostrara en plurales
        db_table = 'sector'  #nombre de creacion de la table
    
#Clase que contiene la informacion del usuario de la base de datos, no contiene la el superADMIN
class Usuario(models.Model):    
    rutUsuario = models.CharField(max_length=12, verbose_name='Rut', null=True)
    nombreUsuario = models.CharField(max_length=12, verbose_name='Nombre', null=True)
    apellidosUsuario = models.CharField(max_length=12, verbose_name='Apellidos', null=True)
    sector = models.ForeignKey(Sector,null=False, on_delete=models.RESTRICT)
    rango = models.ForeignKey(Rango,null=False, on_delete=models.RESTRICT)
    user = models.CharField(max_length=12, verbose_name='Usuarios', default="Anonimo")
    password = models.CharField(max_length=12, verbose_name='Password', default="123")

    def _str_(self):
        return '{} {} - {}'.format(self.rango,self.sector,self.nombreUsuario)
    
    class Meta:
        verbose_name='Usuario'  #como se muestra en tabla
        verbose_name_plural='Usuarios'  #como se mostrara en plurales
        db_table = 'usuario'
        ordering = ['rango','sector','nombreUsuario']
        
