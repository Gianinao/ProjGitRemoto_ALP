#Arthur Leonardo da Silva RM - 559811
#Lucas Guedes Gianini RM - 560454  -Representante-
#Paulo Vinicius de Almeida Figueiredo Medeiros RM - 559768

def main():
    n = int(input("Insira a quantidade de dias que seus dados foram coletados: "))
    meta = 150
    dias_acima_meta = 0
    soma_consumo = 0
    maior_consumo = None
    menor_consumo = None

    for dia in range(1, n + 1):
        consumo = int(input(f"Insira o consumo do dia {dia} (em kWh): "))
        soma_consumo += consumo

        if consumo >= meta:
            dias_acima_meta += 1

        if maior_consumo is None or consumo > maior_consumo:
            maior_consumo = consumo

        if menor_consumo is None or consumo < menor_consumo:
            menor_consumo = consumo
    media_consumo = soma_consumo / n
    dias_abaixo_meta = n - dias_acima_meta

    print("\nRelatório de resultados:")
    if dias_acima_meta == n:
        print("Parabéns, todos os dias cumpriram a meta de consumo sustentável.")
    elif dias_acima_meta == 0:
        print("Infelizmente, nenhum dia cumpriu a meta de consumo sustentável.")
    else:
        print(f"{dias_acima_meta} dias cumpriram a meta e {dias_abaixo_meta} dias não cumpriram a meta.")

    print(f"A média de consumo foi de {media_consumo:.2f} kWh.")
    print(f"O maior consumo foi de {maior_consumo} kWh e o menor consumo foi de {menor_consumo} kWh.")


if __name__ == "__main__":
    main()






