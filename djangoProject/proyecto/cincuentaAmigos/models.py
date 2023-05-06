from django.db import models

"""
Modifaciones para las columnas en las tablas:
-> PrimaryKey: añadimos primary_key = True a la declaración de aatributo
-> unique :  añadimos unique = True a la declaración de aatributo
-> no-autoincrement : No usamos el método models.AutoField, declaramos como models.IntegerField y le añadimos que sea primaryKey
"""

class Categoria(models.Model):
    # INTEGER, PK, AUTOINCREMENT
    id_categoria = models.AutoField(primary_key = True)
    #TEXT, NOT NULL, UNIQUE
    nombre = models.CharField(max_length=50, unique = True)

class Helado(models.Model):
    #INTEGER, PK, AUTOINCREMENT
    id_helado = models.AutoField(primary_key = True)
    #TEXT, NOT NULL, UNIQUE
    sabor = models.CharField(max_length=50, unique = True)

class Mesa(models.Model):
    #INTEGER, PK, (Sin autoincrement)
    numero_mesa = models.IntegerField(primary_key = True )
    #TEXT, NOT NULL
    ubicacion  =  models.CharField(max_length=100)

class Alimento(models.Model):
    #INTEGER, PK, AUTOINCREMENT
    id_alimento= models.AutoField(primary_key = True)
    #INTEGER , FK, NOT NULL
    id_categoria  =  models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #TEXT, NOT NULL, UNIQUE
    nombre  =  models.CharField(max_length=100, unique = True)
    #TEXT, NOT NULL
    imagen  =  models.CharField(max_length=1000)
    #REAL, NOT NULL
    precio  =  models.FloatField()

class Votacion(models.Model):
    #INTEGER, NOT NULL, FK
    numero_mesa  =  models.ForeignKey(Mesa, on_delete=models.CASCADE)
    #INTEGER, NOT NULL, FK
    id_helado  =  models.ForeignKey(Helado, on_delete=models.CASCADE)
    #TEXT, NOT NULL
    nombre_votante  =  models.CharField(max_length=200)

class Carrito(models.Model):
    #INTEGER, NOT NULL, FK
    numero_mesa  =  models.ForeignKey(Mesa, on_delete=models.CASCADE)
    #INTEGER, NOT NULL, FK
    id_alimento  =  models.ForeignKey(Alimento, on_delete=models.CASCADE)

"""
class Orden(models.Model):
"""


"""
class  Grupo(models.Model):
  id_grupo  =  models.AutoField(primary_key=True)

class  Estudiante(models.Model):
  numCta  =  models.IntegerField(default=0, max_length=9)
  nombres  =  models.CharField(max_length=200)
  apellidos  =  models.CharField(max_length=200)
  edad = models.IntegerField(default=0, max_length=3)
  # Cada estudiante guarda el grupo en el que está inscrito
  grupo  =  models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)
"""
