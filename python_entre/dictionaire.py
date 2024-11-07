dictionnaire1={
    0:["F","E","D"],
    1:["un","one","eins"],
2:["deux","two","zwei"],
3:["trois","three","drei"],}
print(dictionnaire1)

key=int(input("entrez 0-3 : "))
print(dictionnaire1[key])


# Créer un dictionnaire vide
utilisateur = {}
langue={}
numero={}
while True:

  flag=input("Entrez les information touche Y , Sortir de toucher N : ")
  if flag=='Y' or 'y':
   langue=input("Langue (F,E,D) : ")
   numero=input("numero: ")
# Ajouter les informations dans le dictionnaire
  utilisateur["langue"] = langue
  utilisateur["numero"] = numero
  continue
else:
 print("\nLes informations de l'utilisateur sont :")

print("saisir le nom")








print(utilisateur)
print(utilisateur.values())