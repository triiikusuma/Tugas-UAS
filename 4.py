dataAngka = [1, 2, 3, [4, 5], [6, [7, 8, 9]]]


def tampilkanAngka(data):
    if isinstance(data, list):
        for angka in data:
            tampilkanAngka(angka)
    else:
        print("Angka",data)


tampilkanAngka(dataAngka)