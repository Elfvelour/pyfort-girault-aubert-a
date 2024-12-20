import json
from random import *

def salle_DE_Tresor(fichier:str):
    with open(fichier,'r',encoding='utf8') as f:
        jeux_tv= json.load(f)
        annee=jeux_tv['Fort Boyard'][randint(0,len(jeux_tv['Fort Boyard'])-1)]
        mot_code=''
        essais=3
        reponse_correcte=False
        return annee
print(salle_DE_Tresor("./data/indicesSalle.json"))
FICHIER="./data/indicesSalle.json"

