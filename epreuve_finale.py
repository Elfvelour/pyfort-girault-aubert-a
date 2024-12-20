import json


def salle_DE_Tresor(fichier:str):
    with open(fichier,'r',encoding='utf8') as f:
        jeux_tv= json.load(f)
        annee=''
        mot_code=''
        essais=3
        reponse_correcte=False
        return  jeux_tv
print(salle_DE_Tresor("./data/indicesSalle.json"))
FICHIER="./data/indicesSalle.json"

