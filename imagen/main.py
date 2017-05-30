##!/usr/bin/python3
# -*- coding: utf-8 -*-

from archivo import Archivo
from pelicula import Pelicula
from imagen import Imagen

pelicula = Pelicula()
imagen=Imagen()
archivo = Archivo(imagen)
archivo2 = Archivo(pelicula)



encontrados = []
encontrados2 = []
encontrados = archivo.buscar("hola")
encontrados2 = archivo2.buscar("duro de matar")
print (archivo.descargar(encontrados),archivo2.descargar(encontrados2))

