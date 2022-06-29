import random
from cola import Cola
from nodo import Nodo

#
def leerMundo():
    mundo = open('test.txt','r')
    tablero = {}
    linea = mundo.readline()
    i = 0

    for l in linea:
        x = l.split