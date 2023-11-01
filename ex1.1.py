# Dezvoltați un script care să implementeze jocul Tic Tac Toe (X și 0). 
# Valorile tablei de joc se vor păstra într-o listă cu 9 elemente, iar cei doi jucători vor introduce pe rând poziția (1-9) pe care vor să o ocupe.

def afisare_tabla(tabla):
    for i in range(0, 9, 3):
        print(tabla[i], "|", tabla[i + 1], "|", tabla[i + 2])

def verifica_castigator(tabla, jucator):
    # Verifică toate posibilitățile de câștig
    linii = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    coloane = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    diagonale = [[0, 4, 8], [2, 4, 6]]

    for linie in linii + coloane + diagonale:
        if all(tabla[i] == jucator for i in linie):
            return True
    return False

def joc_tic_tac_toe():
    tabla = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    jucator_actual = "X"

    for _ in range(9):
        afisare_tabla(tabla)
        pozitie = int(input(f"Jucatorul {jucator_actual}, alege o pozitie (1-9): ")) - 1

        if 0 <= pozitie < 9 and tabla[pozitie] not in ("X", "O"):
            tabla[pozitie] = jucator_actual
        else:
            print("Pozitie invalida. Incearca din nou.")
            continue

        if verifica_castigator(tabla, jucator_actual):
            afisare_tabla(tabla)
            print(f"Jucatorul {jucator_actual} a castigat!")
            break

        jucator_actual = "X" if jucator_actual == "O" else "O"
    else:
        afisare_tabla(tabla)
        print("Jocul s-a incheiat cu rezultat de egalitate.")

if __name__ == "__main__":
    joc_tic_tac_toe()
