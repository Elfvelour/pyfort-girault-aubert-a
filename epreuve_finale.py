import json


def salle_DE_Tresor():
    with open('indicesSalle.json','r',encoding='utf8') as f:
        donnees = json.load(f)
