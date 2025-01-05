#zadanie 1

def podziel_paczki(wagi, max_waga):
     for waga in wagi:
         if waga> max_waga:
             raise ValueError(f"Paczka o wadze {waga} przekraca maksymalną wagę kursu ({max_waga} kg).")

     wagi_sorted = sorted(wagi, reverse = True)
     kursy = []

     for waga in wagi_sorted:
         dodano = False
         for kurs in kursy:
             if sum(kurs) + waga <= max_waga:
                 kurs.append(waga)
                 dodano = True
                 break
         if not dodano:
             kursy.append([waga])
     return len(kursy), kursy

wagi = [20, 5, 8, 15, 10, 10, 7, 8, 9, 16, 9, 25]
max_waga = 25

#print(podziel_paczki(wagi, max_waga))
#liczba_kursow, kursy = podziel_paczki(wagi, max_waga)
#for i, kurs in enumerate (kursy,1):
#     print(f"Kurs {i}: {kurs} \t suma wagi: {sum(kurs)} kg")



#zadanie 2

def bfsStack(graph, start, end):
    visited = []
    queue = [[start]]

    if start == end:
        print("Ten sam węzęł")
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end:
                    print("Najkrótsza ścieżka = ", *new_path)
                    return
            visited.append(node)

    print("Ścieżka nie istnieje")
    return


graph = {
    '1' :['2', '3', '5'],
    '2' :['1', '4'],
    '3' :['1', '5', '6'],
    '4' :['2', '7'],
    '5' :['1', '3', '7'],
    '6' :['3', '8'],
    '7' :['4', '5', '8'],
    '8' :['6', '7']
}

#print(bfsStack(graph, '1', '7'))


#zadanie 3

def optymalizuj_zadania(zadania):
    sorted_zadania = sorted(zadania, key=lambda x: x[1] / x[0], reverse=True)
    res_czas=0
     
    for zadanie in sorted_zadania:
        res_czas+=zadanie[0]
            
    return sorted_zadania, res_czas
#print(optymalizuj_zadania(zadania))


#zadanie 4

def plecak():
    przedmioty = [[10, 25], [5, 8], [13, 20], [15, 28], [9, 18], [4, 16]]
    max_waga_przedmioty = 20

    resultat = []
    res_pieniadze = 0

    sorted_przedmioty = sorted(przedmioty, key=lambda x: x[1] / x[0], reverse=True)
    for przedmiot in sorted_przedmioty:
        if przedmiot[0] <= max_waga_przedmioty:
            resultat.append(przedmiot)
            max_waga_przedmioty -= przedmiot[0]
            res_pieniadze += przedmiot[1]
    print(f"Maksymalna wartość: \t {res_pieniadze}\nWybrane przedmioty: \t {resultat}")
#print(plecak())

#zadanie 5

def activity_selection_procedural(zadania):
    zadania.sort(key=lambda x: x[1])
    
    wybrane_zadania = []
    maks_nagroda = 0
    last_end_time = 0

    for zadanie in zadania:
        poczatek, koniec, nagroda = zadanie
        if poczatek >= last_end_time: 
            wybrane_zadania.append(zadanie)
            maks_nagroda += nagroda
            last_end_time = koniec

    print(f"Maksymalna nagroda: \t {maks_nagroda}\nWybrane zadania: \t {wybrane_zadania}")

zadania = [
        (1, 3, 50),
        (2, 5, 20),
        (4, 6, 70),
        (6, 7, 60),
        (5, 8, 30),
        (7, 9, 40)
    ]

print(activity_selection_procedural(zadania))