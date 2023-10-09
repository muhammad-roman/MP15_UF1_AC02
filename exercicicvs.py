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
    polzada = 2.54
    pound = 0.45
    pesomax = 0.0
    altminim = 10000.0
    base = 0
    escorta = 0
    aler = 0
    ala_pivot = 0
    pivot = 0
    edat20_29 = 0
    edat30_39 = 0
    edat40 = 0

    with open(entrada_csv, 'r', newline='') as f_in, open(sortida_csv, 'w', newline='') as f_out:
        csv_reader = csv.reader(f_in, delimiter=';')
        csv_writer = csv.writer(f_out, delimiter='^')
        #Ex 1
        primera_linea = next(csv_reader)
        primera_linea_cat = [traduccio_cap.get(columna, columna) for columna in primera_linea]
        csv_writer.writerow(primera_linea_cat)
        

        
        #Ex 2
        for fila in csv_reader:
            fila[2] = traduccio_position.get(fila[2], fila[2])
        #Ex 3
            fila[3] = round(float(fila[3])* polzada,2)
            fila[4] = round(float(fila[4])* pound,2)
        
        #Ex 4
            fila[-1] = str(round(float(fila[-1])))

        #Estadisticas
            #a
            if float(fila[4]) > pesomax:
                pesomax = float(fila[4])
            #b
            if float(fila[3]) < altminim:
                altminim = float(fila[3])
            #d
            if fila[2] == "Base":
                base = base +1
            if fila[2] == "Escorta":
                escorta = escorta +1
            if fila[2] == "Aler":
                aler = aler +1
            if fila[2] == "Ala-pivot":
                ala_pivot = ala_pivot +1
            if fila[2] == "Pivot":
                pivot = pivot +1

            #e edades  20-29,30-39,>40    
            if int(fila[-1]) >= 20 and int(fila[-1]) <30:
                edat20_29 = edat20_29 +1
            if int(fila[-1]) >= 30 and int(fila[-1]) <40 :
                edat30_39 = edat30_39 +1
            if int(fila[-1]) >= 40:
                edat40 = edat40 +1

      
            csv_writer.writerow(fila)

        
        print("Pes maxim " + str(pesomax) )
        print("Altura minima "+ str(altminim))
        print ("Hi ha " +str(base)+" bases")
        print ("Hi ha " +str(escorta)+" escortes")
        print ("Hi ha " +str(aler)+" alers")
        print ("Hi ha " +str(ala_pivot)+" ala pivots")
        print ("Hi ha " +str(pivot)+" pivots")
        print ("Hi ha " +str(edat20_29)+" jugadors entre 20 i 29 anys")
        print ("Hi ha " +str(edat30_39)+" jugadors entre 30 i 39 anys")
        print ("Hi ha " +str(edat40)+" jugadors majors que 40 anys")



def main():
    dades = llegir_dades('/home/sjo/Escriptori/DADES/RomanAziz/python_exercices/MP15-UF1-AC02/MP15_UF1_AC02/basket_players.csv')
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
    traductor('/home/sjo/Escriptori/DADES/RomanAziz/python_exercices/MP15-UF1-AC02/MP15_UF1_AC02/basket_players.csv', 'jugadors_basket.csv', dict_traduccio_cap, dict_traduccio_position)




main()

