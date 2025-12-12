from festivales import *

ruta = ("data/festivales.csv")

#Apartado 1
res = lee_festivales(ruta)
for e in res:
    print(e)