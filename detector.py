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


def ler_lista():
    """Pede uma lista válida e repete a pergunta quando a entrada é inválida."""
    while True:
        entrada = input("\nDigite a lista (números separados por vírgula): ").strip()

        try:
            partes = [item.strip() for item in entrada.split(",")]

            if not entrada or any(not item for item in partes):
                raise ValueError

            lista = [int(item) for item in partes]

            if len(lista) < 2:
                print("❌ Informe pelo menos 2 números. Vamos tentar de novo.")
                continue

            return lista

        except ValueError:
            print("❌ Lista inválida! Use apenas números inteiros separados por vírgulas.")
            print("Exemplo: 2, 3, 5, 7, 11")


def ler_posicao():
    """Pede uma posição positiva e não deixa o programa encerrar por erro."""
    while True:
        try:
            posicao = int(input("Qual posição você quer descobrir? "))

            if posicao < 1:
                print("❌ A posição precisa ser maior que zero.")
                continue

            return posicao

        except ValueError:
            print("❌ Digite uma posição usando um número inteiro.")


def analisar_lista(lista):
    """Identifica o padrão e exibe o termo solicitado."""
    # 1. Números ao quadrado (n²).
    if all(lista[i] == (i + 1) ** 2 for i in range(len(lista))):
        print("\n✅ Padrão detectado: Números ao Quadrado (n²)")
        pos = ler_posicao()
        print(f"O número na posição {pos} é: {pos ** 2}")
        return True

    # 2. Números primos consecutivos.
    if eh_sequencia_de_primos(lista):
        print("\n✅ Padrão detectado: Sequência de números primos consecutivos!")
        pos = ler_posicao()

        if pos <= len(lista):
            resultado = lista[pos - 1]
        else:
            resultado = lista[-1]
            for _ in range(pos - len(lista)):
                resultado = proximo_primo(resultado)

        print(f"O número primo na posição {pos} é: {resultado}")
        return True

    # 3. Sequência linear.
    diffs = [lista[i + 1] - lista[i] for i in range(len(lista) - 1)]

    if all(d == diffs[0] for d in diffs):
        razao = diffs[0]
        ajuste = lista[0] - razao
        sinal = "+" if ajuste >= 0 else "-"
        print("\n✅ Padrão detectado: Sequência Linear!")
        print(f"A fórmula é: {razao}n {sinal} {abs(ajuste)}")

        pos = ler_posicao()
        print(f"O número na posição {pos} é: {(razao * pos) + ajuste}")
        return True

    # 4. Sequência de 2º grau.
    if len(lista) >= 3:
        segunda_diff = [
            diffs[i + 1] - diffs[i]
            for i in range(len(diffs) - 1)
        ]

        if all(sd == segunda_diff[0] for sd in segunda_diff):
            print("\n✅ Padrão detectado: Sequência de 2º Grau")
            print("A segunda diferença é constante:", segunda_diff[0])

            pos = ler_posicao()
            a1 = lista[0]
            d1 = diffs[0]
            d2 = segunda_diff[0]

            resultado = (
                a1
                + (pos - 1) * d1
                + ((pos - 1) * (pos - 2) * d2) // 2
            )

            print(f"O número na posição {pos} é:\n\n{resultado}")
            return True

    print("\n❌ Não consegui identificar um padrão conhecido nessa lista.")
    return False


def descobrir_padrao():
    print("v1.2.1")
    print("-- Detector de padrões matemáticos --")

    while True:
        lista = ler_lista()

        if not analisar_lista(lista):
            print("Tudo bem! Digite outra lista para tentar novamente.")
            continue

        continuar = input("\nDeseja analisar outra sequência? (s/n): ").strip().lower()
        if continuar not in ("s", "sim"):
            print("\nAté a próxima! 👋")
            break


if __name__ == "__main__":
    try:
        descobrir_padrao()
    except (KeyboardInterrupt, EOFError):
        print("\n\nPrograma encerrado.")
