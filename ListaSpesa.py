lista = []
def aggiungi():
    elementi = int(input("Quanti elementi vuoi aggiungere alla lista? "))
    for i in range(elementi):
        prodotto = input("Inserisci prodotto: ")
        lista.append(prodotto)

def visualizza():
    print(lista)

def elimina():
    id = int(input("Inserisci l'id del prodotto da eliminare: "))
    lista.pop(id - 1)

def conta():
    print(len(lista))
    

while True:
    scelta = int(input("0. Esci\n1. Aggiungi elemento\n2. Elimina elemento\n3. Visualizza lista\n4. Conta elementi "))
    if scelta == 0:
        break
    elif scelta == 1:
        aggiungi()
    elif scelta == 2:
        elimina()
    elif scelta == 3:
        visualizza()
    elif scelta == 4:
        break
    else:
        print("Opzione non valida")
