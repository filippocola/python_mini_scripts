# il pattern matching non è altro che uno switch-case. 

if __name__ == "__main__":
    subjectValue: list[str] = ["primo", "secondo"]
    match subjectValue:
        case [p, s]:
            print(f"Trovato {p} e {s}")

    subjectValue2: list[str, int] = ["dispari", 51]
    match subjectValue2:
        case ["pari", valore] if int(valore) % 2 == 0:
            print(f"{valore} è un numero pari")
        case ["dispari", valore] if int(valore) % 2 != 0:
            print(f"{valore} è un numero dispari")
        case _: 
            print("C'è un errore dei dati")