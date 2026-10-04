import tkinter as tk
import random


filas = 5
columnas = 5
numero_minas = 5
direcciones = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0,-1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

tablero = []

for fila in range(filas):
    nueva_fila = []

    for columna in range(columnas):
        nueva_fila.append(0)

    tablero.append(nueva_fila)


minas_colocadas = 0

while minas_colocadas < numero_minas:
    fila_mina = random.randint(0, filas - 1)
    columna_mina = random.randint(0, columnas - 1)
    if tablero[fila_mina][columna_mina] == 0:
        tablero[fila_mina][columna_mina] = -1
        minas_colocadas += 1

for fila in range(filas):
    for columna in range(columnas):
        if tablero[fila][columna] == -1:
            continue
        minas_cerca= 0
        for desplazamiento_columna, desplazamiento_fila in direcciones:
            fila_vecina = fila + desplazamiento_fila
            columna_vecina = columna + desplazamiento_columna
            if 0 <= fila_vecina <filas and 0 <= columna_vecina <columnas:
                if tablero [fila_vecina][columna_vecina] == -1:
                    minas_cerca+= 1
        tablero [fila][columna]= minas_cerca

for fila in tablero:
    print(fila)

ventana = tk.Tk()
ventana.title("Buscaminas")

ventana.mainloop()