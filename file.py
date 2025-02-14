inventario = {
0 : {"nome": "Il PC di ...", "quantità": 1, "prezzo": 3999},
1 : {"nome": "Nintendo Switch 2", "quantità": 10, "prezzo": 449},
2 : {"nome": "GTA VI", "quantità": 3, "prezzo": 100}
}
def aggiunzione():
    chiave = len(inventario) + 1 
    nome = input("inserisci in nome")
    quantità = (input("inserisci la quantità"))
    prezzo = int(input("inserisci iil prezzo"))
    invenrtario[chiave] = {"nome": nome , "quantità" :quantità , "prezzo" : prezzo}
    print(aggiunzione)