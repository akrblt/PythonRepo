
num1=input("Bonjour , J'attends un premier nombre entre 5 et 30 : ")
print("Le nombre 1: "+num1)


num2=input("Bonjour , J'attends un second nombre entre 5 et 30 , different du premier : "+num1+"  :")
print("Le nombre 2: "+num2)
min=0
max=0
if num1<num2:
    max=int(num1)
    min=int(num2)
else:
    max=int(num2)
    min=int(num1)

print(f"Donc j'ai compris , je vais travailler avec min = {min}  et max = {max}")
print(f"Le produit de {min} par {max} donne : {(min)*(max)}")

print(f"Et on puet l'illustrer par le rectangle suivant de {min}  lignes de {max} etoiles: ")
for i in range(min):
    print("*"*max)
print(f"Voici les nombres entres  {min} et {max}")
for i in range(min,max+1):
    print(i,end=" ")
print(" ")
print(f"Leur somme est:  {sum(range(min,max+1))} , on peut l'illustrier par la figure suivante de {sum(range(min,max+1))} etoiles;")
for i in range(min,max+1):
    print(f"{i}: {"*"*i}")