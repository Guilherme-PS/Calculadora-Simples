def menu():
    while True:
        answer = input("\033[1m> Deseja Continuar? [S/N] \033[0m").upper()
        if answer == "S":
            break
        elif answer == "N":
            exit()
        else:
            print("Opção Inválida!")

def choose_op() -> str:
    num_op = {str(x+1): y for x, y in enumerate(operations.keys())}
    while True:
        op = input("Digite o Número/Nome da Operação: ").title()
        if op in num_op.keys():
            op = num_op.get(op)
            return op
        elif op in operations.keys():
            return op
        else:
            print("Operador Inválido!")


operations = {"Adição": lambda x, y: x + y,
              "Subtração": lambda x, y: x - y,
              "Multiplicação": lambda x, y: x * y,
              "Divisão": lambda x, y: x / y,
              "Exponenciação": lambda x, y: x ** y,
              "Módulo": lambda x, y: x % y}

while True:
    print("-" * 33)
    for i, j in enumerate(operations.keys()):
        print(f" {i+1} : {j}")
    print("-" * 33)

    op_name = choose_op()

    print(f"\033[1m> {op_name}\033[0m")
    num_1 = float(input("Digite o 1° Número: "))
    while True:
        num_2 = float(input("Digite o 2° Número: "))
        if op_name == "Divisão" and num_2 == 0:
            print("Divisão por Zero!")
        else:
            break

    for i, j in operations.items():
        if op_name == i:
            print("-" * (22 + len(op_name) + len(str(j(num_1, num_2)))))
            print(f"\033[1m O Resultado da {op_name} é: {j(num_1, num_2):.2f}\033[0m")
            print("-" * (22 + len(op_name) + len(str(j(num_1, num_2)))))
            break
    menu()