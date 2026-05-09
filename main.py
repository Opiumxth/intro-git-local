from comparacion import comparar

def main():
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese otro número: "))

        if comparar(a, b) == 1:
                print(f"{a} es mayor que {b}")
        elif comparar(a, b) == 2:
                print(f"{b} es mayor que {a}")
        elif comparar(a, b) == 0:
                print("Ambos números son iguales")

if __name__ == "__main__":
        main()