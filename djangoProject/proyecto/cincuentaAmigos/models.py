from django.db import models

# Autor: EDIS

"""
Modifaciones para las columnas en las tablas:
-> PrimaryKey: añadimos primary_key = True a la declaración de atributo.
-> unique :  añadimos unique = True a la declaración de aatributo.
-> no-autoincrement : No usamos el método models.AutoField, declaramos como models.IntegerField y le añadimos que sea primaryKey.
"""

class Categoria(models.Model):
    # INTEGER, PK, AUTOINCREMENT
    id_categoria = models.AutoField(primary_key = True)
    #TEXT, NOT NULL, UNIQUE
    nombre = models.CharField(max_length=50, unique = True)
    #TEXT, NOT NULL
    imagen  =  models.CharField(max_length=1000)

class Helado(models.Model):
    #INTEGER, PK, AUTOINCREMENT
    id_helado = models.AutoField(primary_key = True)
    #TEXT, NOT NULL, UNIQUE
    sabor = models.CharField(max_length=50, unique = True)
    #TEXT, NOT NULL
    imagen  =  models.CharField(max_length=1000)
    #TEXT, NOT NULL
    descripcion  =  models.CharField(max_length=100)

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
    #TEXT, NOT NULL
    descripcion  = models.CharField(max_length=1000)

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
    #INTEGER, NOT NULL
    cantidad = models.IntegerField()
