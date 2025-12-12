from collections import defaultdict
import csv
from datetime import date, datetime, time
from typing import Counter, NamedTuple
 
Artista = NamedTuple("Artista",     
                        [("nombre", str), 
                        ("hora_comienzo", time), 
                        ("cache", int)])

Festival = NamedTuple("Festival", 
                        [("nombre", str),
                        ("fecha_comienzo", date),
                        ("fecha_fin", date),
                        ("estado", str),                      
                        ("precio", float),
                        ("entradas_vendidas", int),
                        ("artistas", list[Artista]),
                        ("top", bool)
                    ])

def lee_festivales (archivo:str)->list[Festival]:
    with open(archivo, encoding="utf-8") as f:
        lista = []
        lector = csv.reader(f)
        next(lector)
        for nombre, fecha_comienzo, fecha_fin, estado, precio, entradas_vendidas,artistas, top in lector:
            fecha_comienzo = datetime.strptime(fecha_comienzo, "%Y-%m-%d").date()
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
            precio = float(precio)
            entradas_vendidas = int(entradas_vendidas)
            artistas = parsea_artistas(artistas)
            top = parsea_top(top)    
            lista_festival = Festival(nombre, fecha_comienzo,fecha_fin,estado,precio,entradas_vendidas,artistas,top)
            lista.append(lista_festival)
    return lista


def parsea_artistas(artistas:str)->list[Artista]:
    lista=[]
    partes = artistas.split("-")
    for artista in partes:
        parte_limpia = artista.strip()
        if parte_limpia:
            festivales_parseado = parsea_festivales(parte_limpia)
            lista.append(festivales_parseado)
    return lista

def parsea_festivales(artistas:str)->Artista:
    nombre,hora_comienzo,cache = artistas.split("_")
    return Artista(nombre,datetime.strptime(hora_comienzo, "%H:%M"),int(cache))


def parsea_top(top:str)->bool:
    valor = top.strip().lower()
    return valor in ("1","sí","true")

def total_facturado(festivales:list[Festival], fecha_ini:date|None=None, fecha_fin:date|None=None)->float:
    total = 0.0
    for festival in festivales:
        if (fecha_ini == None or fecha_ini <= festival.fecha_comienzo) and (fecha_fin == None or fecha_fin >= festival.fecha_fin):
            if festival.estado == "CELEBRADO":
                total += ((festival.entradas_vendidas*festival.precio))
    return total

def artista_top(festivales: list[Festival]) -> tuple[int, str]:
    dicc = defaultdict(int)
    for festival in festivales:
        if festival.estado == "CELEBRADO":
            for artistas in festival.artistas :
                dicc[artistas.nombre] += 1
    return max(dicc.items(), key = lambda t:t[1])

def mes_mayor_beneficio_medio(festivales: list[Festival]) -> str:
    
    
   
def MESES(festival:Festival)->str:
        
            