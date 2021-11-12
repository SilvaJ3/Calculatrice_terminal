nombre1 = input("Entrez un premier nombre : ")
nombre2 = input("Entrez un deuxième nombre : ")

while not nombre1.isdigit() or not nombre2.isdigit():
    print("Veuillez entrez deux nombres valides")
    nombre1 = input("Entrez un premier nombre :")
    nombre2 = input("Entrez un deuxième nombre :")
else:
    print(f"Le resultat de l'addition de {nombre1} avec {nombre2} est égal à {int(nombre1) + int(nombre2)}")