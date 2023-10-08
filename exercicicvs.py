import csv

#Extract
def llegir_dades(nom_fitxer):
    dades = []
    with open(nom_fitxer, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            dades.append(row)
    return dades



def print_dades(dades):
    for i, jugador in enumerate(dades):
        print(f"Jugador {i}:")
        for camp, valor in jugador.items():
            print(f"{camp}: {valor}")
        print("=" * 20)



#Transform
def traductor(entrada_csv, sortida_csv, traduccio_cap, traduccio_position):
    with open(entrada_csv, 'r', newline='') as f_in, open(sortida_csv, 'w', newline='') as f_out:
        csv_reader = csv.reader(f_in, delimiter=';')
        csv_writer = csv.writer(f_out, delimiter=';')
        #Ex 1
        primera_linea = next(csv_reader)
        primera_linea_cat = [traduccio_cap.get(columna, columna) for columna in primera_linea]
        csv_writer.writerow(primera_linea_cat)
        
        #Ex 2
        for fila in csv_reader:
            fila[2] = traduccio_position.get(fila[2], fila[2])
        #Ex 4
            fila[-1] = str(round(float(fila[-1])))
            csv_writer.writerow(fila)


def main():
    dades = llegir_dades('basket_players.csv')
    print_dades(dades)
#Dict ex 1
    dict_traduccio_cap = {
        "Name":"Nom",
        "Team": "Equip",
        "Position": "Posicio",
        "Heigth": "Alcada",
        "Weigth": "Pes",
        "Age": "Edat"
    }
#Dict ex 2
    dict_traduccio_position = {
        "Point Guard":"Base",
        "Shooting Guard":"Escorta",
        "Small Forward":"Aler",
        "Power Forward":"Ala-pivot",
        "Center":"Pivot"
    }
    traductor('basket_players.csv', 'basket_platers_ESP.csv', dict_traduccio_cap, dict_traduccio_position)

main()