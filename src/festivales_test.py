from festivales import *

ruta = ("data/festivales.csv")

#Apartado 1
res = lee_festivales(ruta)
for e in res:
    print(e)
    
#Apartado 2
#Fecha_ini = None, feca_fin= None
fecha_ini = None;fecha_fin = None
total = total_facturado(res, fecha_ini, fecha_fin)
print(f"Entre {fecha_ini} y {fecha_fin} el total es {total}")

#Fecha_ini = None, feca_fin= xxx
fecha_ini = None;fecha_fin="2024-6-15"
fecha_fin = datetime.strptime(fecha_fin,"%Y-%m-%d").date()
total = total_facturado(res, fecha_ini, fecha_fin)
print(f"Entre {fecha_ini} y {fecha_fin} el total es {total}")

#Fecha_ini = xxx, fecha_fin = None
fecha_ini = "2024-6-15";fecha_fin=None
fecha_ini = datetime.strptime(fecha_ini,"%Y-%m-%d").date()
total = total_facturado(res, fecha_ini, fecha_fin)
print(f"Entre {fecha_ini} y {fecha_fin} el total es {total}")

#Fecha_ini = xxx, fecha_fin = xxx
fecha_ini = "2024-6-1";fecha_fin="2024-6-15"
fecha_fin = datetime.strptime(fecha_fin,"%Y-%m-%d").date()
fecha_ini = datetime.strptime(fecha_ini,"%Y-%m-%d").date()
total = total_facturado(res, fecha_ini, fecha_fin)
print(f"Entre {fecha_ini} y {fecha_fin} el total es {total}")

#Apartado 3
artista = artista_top(res)
print(f"El artista que ha actuado en más festivales es {artista}")