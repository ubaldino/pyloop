#!/usr/bin/python2
#-*- coding: utf-8 -*-
#ubaldino zurita
import sys, urllib2, re, urllib

def report_hook(block_count, block_size, total_size):
  total_kb = total_size / 1024
  descargado = block_count * (block_size / 1024)
  porcentaje = descargado * 100 / total_kb
  texto_barra =  "=> " + str(descargado) + " kb de " + str(total_kb / 1024.0) + " Mb (" + str(porcentaje) + "%)"
  sys.stdout.write("\b" * (len(texto_barra)))
  sys.stdout.write(texto_barra)
  sys.stdout.flush()

# comprobando si se ingreso el dato requerido
if len(sys.argv) > 1:
  art = sys.argv[1]; url = "http://www.goear.com/search/%s"%(art)
  try: html = str(urllib2.urlopen(url).read())
  except: print "\033[1;31m **** Error de connexión ****"
  else:
    # obteniendo el rango de paginas
    found = re.findall("(\d*)\Waudios</a>", html)
    if int(found[0])==1000: ult_pag = 99
    else: ult_pag=int(found[0])/10
    if ult_pag==0: ult_pag=1
    print "intervalo de paginas: 1 - %d"%(ult_pag)
    html = str(urllib2.urlopen("%s/%d"%(url,2)).read())
    number_tema=0
    while number_tema == 0:
      pag = int(raw_input('elija el numero de pagina q quiera: '))
      # Estructura el listado de temas
      html = str(urllib2.urlopen( "%s/%d/recent"%(url,pag)).read() )
      ids_music = re.findall( "listen/(\w{7,})/[a-z0-9\-]{1,}", html )
      nombres_music = re.findall( "listen/\w{7,}/([\d\w\-]{1,})", html )
      i=0
      for dat in nombres_music: i = i+1; print "\033[1;33m %d\t\033[1;37m%s"%(i, dat)
      print "\n"
      number_tema = int(raw_input('eliga un tema por su numero o cero para regresar: '))
    # prepara para descargar el archivo .mp3
    try:
      url_desc = "http://www.goear.com/action/sound/get/%s"%(ids_music[number_tema-1])
      print "\033[1;36m[descargando]\033[1;34m %s.mp3\033[1;00m"%(str(nombres_music[number_tema-1]))
      urllib.urlretrieve( url_desc,"%s.mp3"%(str(nombres_music[number_tema-1])),reporthook=report_hook)
    except: print "No se descargo el archivo / mala elección"
    else: print "\t\033[1;31mdescarga finalizada\033[1;00m"
else: print """
\033[1;37m Ejemplo para el uso del script:

------------------------------
\033[1;31m./goear.py <nombre-artista>
./goear.py <nombre-grupo>
\033[1;37m------------------------------

Los espacios en blanco deben ser reeemplazados
por guiones.
Talvez algun dia le ponga opciones\033[1;00m
"""
