#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from os import listdir
from os.path import isfile, isdir


class RECUP:
	def __init__(self):
		pass

	def main(self):
		os.system("clear")
		c = "| HOLA %s este es el ATENEA un sistema de "% self.ObtenerNombre()
		c += "búsqueda y copia de archivos. |" 
		print self.ObtenerCabecera(self.ObtenerDigitos(c))
		print c
		cadena = "| Con este sistema podremos ordenar todos los archivos que "
		cadena += "encontremos, cuyo sujeto que está a tu lado borró. Se "
		cadena += "ordenará por tipos de archivos (imágenes en un lado,"
		cadena += "archivos en otro y esperar que encontremos archivos que "
		cadena += "sean importantes para ti)."
		print self.Contenido(self.ObtenerDigitos(c), cadena)
		print self.ObtenerCabecera(self.ObtenerDigitos(c))
		cadena = "| POR FAVOR PRESIONA ENTER PARA CONTINUAR (el sistema empeza"
		cadena += "rá a trabajar automáticamente regresa en un buen rato, te "
		cadena += "avisaré cuando termine.) :)"
		print self.Contenido(self.ObtenerDigitos(c), cadena)
		print self.ObtenerCabecera(self.ObtenerDigitos(c))
		print raw_input()
		os.system("clear")
		self.inicio()

	def Contenido(self, c, cadena):
		wa = False
		ca = len(cadena)
		cx = c
		c = c - 4
		retorno = ""
		cont = 0
		for a in range(0, ca):
			cont += 1
			if self.estope(c, cont):
				retorno += cadena[a]
				if len(retorno) > cx:
					retorno = "%s%s" % (retorno, "|")
				else:
					retorno = "%s%s" % (retorno, "  |")

				retorno += "\n%s" % "| "
				cont = 0
			else:
				retorno += cadena[a]
		return retorno

	def estope(self, c, a):
		if(c == a):
			return True
		else:
			return False

	def ObtenerNombre(self):
		ax = os.popen("who").read()
		ax = ax.split(" ")
		return ax[0]

	def ObtenerCabecera(self, c):
		ca = ""
		for a in range(0, int(c) - 3):
			ca += "-"
		ca = "%s%s%s" % ("+", ca, "+")
		return ca

	def ObtenerDigitos(self, c):
		return len(c)

	def inicio(self):
		os.system("mkdir /mnt/img")
		os.system("mkdir /mnt/docs")
		os.system("mkdir /mnt/music")
		os.system("mkdir /mnt/otros")

		for cosa in listdir("."):
			cosa = cosa.replace(" ", "\ ")
			cosa = cosa.replace("(", "\( ")
			cosa = cosa.replace(")", "\) ")
			if isdir(cosa):
				print "%s" % cosa
				os.system("cd %s" % cosa)
				pwd = os.getcwd()
				extimg = [".jpg", ".jpeg", ".JPG", ".JPEG", ".PNG", ".png",
						".gif", ".GIF", ".bmp", ".BMP"]
				extdoc = [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
						".DOC", ".DOCX", ".XLS", ".XLSX", ".PPT", ".PPTX",
						".pdf",	".PDF", ".ods", ".ODS", ".ODT", ".odt",
						".ODP", ",odp"]
				extmus = [".mp3", ".wav", ".MP3", ".mp4", ".WAV", ".MP4",
						".OGG", ".ogg", ".mov", ".MOV", ".WMV", ".wmv"]
				for contenedor in listdir("%s%s%s" % (pwd, "/", cosa)):
					contenedor = contenedor.replace(" ", "\ ")
					contenedor = contenedor.replace("(", "\(")
					contenedor = contenedor.replace(")", "\)")
					prex = contenedor[len(contenedor) - 4:len(contenedor)]
					if prex in extimg:
						os.system("%s%s%s" % ("mv ", "%s%s%s%s%s" % (pwd, "/",
						cosa, "/", contenedor), " /mnt/img"))
						print "%s%s" % (contenedor, " >> img")
					elif prex in extdoc:
						os.system("%s%s%s" % ("mv ", "%s%s%s%s%s" % (pwd, "/",
						cosa, "/", contenedor), " /mnt/docs"))
						print "%s%s" % (contenedor, " >> docs")
					elif prex in extmus:
						os.system("%s%s%s" % ("mv ", "%s%s%s%s%s" % (pwd, "/",
						cosa, "/", contenedor), " /mnt/music"))
						print "%s%s" % (contenedor, " >> music")
					else:
						os.system("%s%s%s" % ("mv ", "%s%s%s%s%s" % (pwd, "/",
						cosa, "/", contenedor), " /mnt/otros"))
						print "%s%s" % (contenedor, " >> otros")
		os.system("totem culminacion.mp3")
if __name__ == "__main__":
	if os.geteuid() != 0:
		print "\n     Agregale 'sudo' para iniciar.\n"
		sys.exit(1)
	else:
		recuperar = RECUP()
		recuperar.main()
