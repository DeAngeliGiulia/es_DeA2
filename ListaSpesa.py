lista = []
def aggiungi():
    elementi = int(input("Quanti elementi vuoi aggiungere alla lista? "))
    for i in range(elementi):
        prodotto = input("Inserisci prodotto: ")
        lista.append(prodotto)

def visualizza():
    print(lista)
    
aggiungi()
visualizza()