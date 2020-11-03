import random

listNombres = []
listSize = 5

# Générer nombres aléatoires


def genererNombres():
    for i in range(listSize):
        nombre = random.randint(-1000, 1000)
        listNombres.append(nombre)


# Vérifier la division des nombres


def diviserNombre(nombre):
    if (nombre % 3 == 0) and (nombre % 5 == 0):
        return 'Gestform'
    elif nombre % 3 == 0:
        return 'Geste'
    elif nombre % 5 == 0:
        return 'Forme'
    else:
        return nombre

# Afficher la liste des nombres


def afficherNombres():
    genererNombres()
    print("\nListe des nombres : " + " | ".join(str(n)
                                                for n in listNombres))
    print("Divisible par 3 (Geste), par 5 (Forme) ou les deux (Gestform) \n")
    for nombreDivisible in listNombres:
        print(str(nombreDivisible) + " ==> " +
              str(diviserNombre(nombreDivisible)))


afficherNombres()
