def eh_primo(n):
    """Retorna True quando n é um número primo."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2

    return True


def proximo_primo(n):
    """Encontra o primeiro número primo maior que n."""
    candidato = n + 1
    while not eh_primo(candidato):
        candidato += 1
    return candidato


def eh_sequencia_de_primos(lista):
    """Verifica se a lista contém primos consecutivos em ordem crescente."""
    if not all(eh_primo(numero) for numero in lista):
        return False

    return all(
        proximo_primo(lista[i]) == lista[i + 1]
        for i in range(len(lista) - 1)
    )


def descobrir_padrao():
    print("v1.2.0")
    print("-- Detector de padrões matemáticos --\n")

    entrada = input("Digite a lista: ")

    try:
        lista = [int(x.strip()) for x in entrada.split(",") if x.strip()]

        if len(lista) < 2:
            print("Mínimo de 2 números.")
            return

        # 1. Vê se é uma sequência de quadrados perfeitos (n²).
        if all(lista[i] == (i + 1) ** 2 for i in range(len(lista))):
            print("\n✅ Padrão detectado: Números ao Quadrado (n²)")
            pos = int(input("Qual posição você quer descobrir? "))
            if pos < 1:
                print("❌ A posição deve ser maior que zero.")
                return
            print(f"O número na posição {pos} é: {pos ** 2}")
            return

        # 2. Detecta uma sequência de números primos consecutivos.
        if eh_sequencia_de_primos(lista):
            print("\n✅ Padrão detectado: Sequência de números primos consecutivos!")
            pos = int(input("Qual posição você quer descobrir? "))

            if pos < 1:
                print("❌ A posição deve ser maior que zero.")
                return

            # Usa os termos informados e continua a sequência, se necessário.
            resultado = lista[-1]
            if pos <= len(lista):
                resultado = lista[pos - 1]
            else:
                for _ in range(pos - len(lista)):
                    resultado = proximo_primo(resultado)

            print(f"O número primo na posição {pos} é: {resultado}")
            return

        # 3. Vê se é uma sequência linear.
        diffs = [lista[i + 1] - lista[i] for i in range(len(lista) - 1)]

        if all(d == diffs[0] for d in diffs):
            razao = diffs[0]
            ajuste = lista[0] - razao
            sinal = "+" if ajuste >= 0 else "-"
            print("\n✅ Padrão detectado: Sequência Linear!")
            print(f"A fórmula é: {razao}n {sinal} {abs(ajuste)}")

            pos = int(input("Qual posição você quer descobrir? "))
            if pos < 1:
                print("❌ A posição deve ser maior que zero.")
                return
            print(f"O número na posição {pos} é: {(razao * pos) + ajuste}")
            return

        # 4. Detecta uma sequência de 2º grau.
        if len(lista) >= 3:
            segunda_diff = [
                diffs[i + 1] - diffs[i]
                for i in range(len(diffs) - 1)
            ]

            if all(sd == segunda_diff[0] for sd in segunda_diff):
                print("\n✅ Padrão detectado: Sequência de 2º Grau")
                print("Dica: Aumenta de", segunda_diff[0], "em", segunda_diff[0])

                pos_alvo = int(input("Qual posição você quer prever? "))
                if pos_alvo < 1:
                    print("❌ A posição deve ser maior que zero.")
                    return

                a1 = lista[0]
                d1 = diffs[0]
                d2 = segunda_diff[0]
                n = pos_alvo

                # Fórmula da sequência de 2º grau.
                resultado = (
                    a1
                    + (n - 1) * d1
                    + ((n - 1) * (n - 2) * d2) // 2
                )

                print(f"O número na posição {pos_alvo} é:\n\n{resultado}")
                return

        print("\n❌ Padrão não identificado pelos detectores disponíveis.")

    except ValueError:
        print("\n❌ Digite somente números inteiros separados por vírgulas.")


if __name__ == "__main__":
    descobrir_padrao()
