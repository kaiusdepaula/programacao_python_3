#For this one I'll write the program to write in portuguese
from random import randint, choice

artigos = (
    "o", "os", "a", "as", "um", "uns", "uma", "umas"
)
sujeitos = (
    "Pinguim", "Bicicleta", "Fino", "Estrada",
    "Soldado", "Fantasma", "Torta", "Estranho",
    "Guitarra", "Tambor", "Mar", "Tambor",
    "Ovos", "Seis", "Ruim", "Iogurte", "Uva", "Joelho"
)

verbos = (
    "criou", "viveu", "amou", "dançou",
    "viajou", "desceu", "subiu", "venceu",
    "animou", "queria", "fez", "gostou"
)
adverbios = (
    "animadamente", "felizmente", "tristemente",
    "constantemente", "rapidamente", "diferentemente",
    "contrariamente", "curiosamente", "contentemente"
)

for _ in range(1, 6):
    artigo = choice(artigos)
    sujeito = choice(sujeitos)
    verbo = choice(verbos)
    adverbio = choice(adverbios)
    if randint(0, 1) == 0:
        print(artigo, sujeito, verbo)
    else:
        print(artigo, sujeito, verbo, adverbio)