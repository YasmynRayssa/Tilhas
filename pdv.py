compras = []
total_bruto = 0
total_final = 0

while True:
    print("\n========== PONTO DE VENDA DA LOJA ==========")
    print("1 - Registrar compra")
    print("2 - Ver resumo das compras")
    print("0 - Encerrar")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break

    elif opcao == "1":
        valor = float(input("Valor da compra (0 para encerrar): R$ "))

        while valor < 0:
            print("O valor não pode ser negativo.")
            valor = float(input("Digite o valor novamente (0 para encerrar): R$ "))

        if valor == 0:
            break

        idade = int(input("Idade do cliente: "))

        while idade < 0:
            print("A idade não pode ser negativa.")
            idade = int(input("Digite a idade novamente: "))

        final = valor

        if idade >= 65:
            final = final * 0.80

        if final > 100:
            final = final * 0.90

        final = round(final, 2)
        compras.append([valor, final])
        total_bruto = total_bruto + valor
        total_final = total_final + final

        print("\nResumo parcial das compras!")
        print(f"\1nValor original: R$ {valor:.2f}")
        print(f"Desconto total: R$ {valor - final:.2f}")
        print(f"Valor final: R$ {final:.2f}")
        print("Compra registrada!")

    elif opcao == "2":
        print("\nResumo Final das compras")
        print("Quantidade de compras:", len(compras))
        print(f"Total bruto: R$ {total_bruto:.2f}")
        print(f"Total de descontos: R$ {total_bruto - total_final:.2f}")
        print(f"Total final: R$ {total_final:.2f}")

    else:
        print("Opção inválida. Escolha 1, 2 ou 0.")

print("\nResumo final do dia")
print("Quantidade de compras:", len(compras))
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_bruto - total_final:.2f}")
print(f"Total final: R$ {total_final:.2f}")
print("Programa encerrado.")
