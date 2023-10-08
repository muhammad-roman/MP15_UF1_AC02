import csv

def llegir_dades(nom_fitxer):
    dades = []
    with open(nom_fitxer, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            dades.append(row)
    return dades

dades = llegir_dades('basket_players.csv')

for i, jugador in enumerate(dades):
    print(f"Jugador {i}:")
    for camp, valor in jugador.items():
        print(f"{camp}: {valor}")
    print("=" * 20)