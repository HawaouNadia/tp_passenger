import copy 
print ("Bienvenue à Touristique")
#création des bus
bus = {
    "id_bus" : " ",
    "nbreDePlaces" : 70,
    "tableauPassager":" "
}

#création des passagers 
passager = {
    "id_passager" : 0,
    "nom_passager" : " ",
    "poidsBagages" : 0.0
}

#initialisation du tableau des passagers
listPassagers = []


passagerActuel=copy.deepcopy(passager)
number=int(input("Combien de passagers souhaitez vous enregistrer?"))
for i in range (0,number):

    passagerActuel ["id_passager"] = int(input("Quel est l'identifiant du passager? "))
    passagerActuel ["nom_passager"] = input("Veuillez entrer le nom du passager : ")
    passagerActuel ["poidsBagages"] = float(input("Quel est le poids des bagages? "))
    listPassagers.append(passagerActuel)
    print ("le voyageur {} ayant {}kgs de bagages a pour identifiant {}!".format(passagerActuel ["nom_passager"],passagerActuel ["poidsBagages"],passagerActuel ["id_passager"]))
