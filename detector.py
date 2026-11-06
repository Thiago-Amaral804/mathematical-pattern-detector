from math import isqrt


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


def identificar_quadrados(lista):
    """Retorna a raiz do primeiro quadrado se forem quadrados consecutivos."""
    raizes = [isqrt(numero) for numero in lista]

    if all(raiz * raiz == numero for raiz, numero in zip(raizes, lista)):
        if all(raizes[i + 1] == raizes[i] + 1 for i in range(len(raizes) - 1)):
            return raizes[0]

    return None


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
            posicao = int(input("\nQual termo você quer descobrir? "))

            if posicao < 1:
                print("❌ A posição precisa ser maior que zero.")
                continue

            return posicao

        except ValueError:
            print("❌ Digite uma posição usando um número inteiro.")


def analisar_lista(lista):
    """Identifica o padrão, mostra sua fórmula e calcula o termo escolhido."""

    # 1. Quadrados perfeitos consecutivos, começando em qualquer raiz.
    primeira_raiz = identificar_quadrados(lista)

    if primeira_raiz is not None:
        print("\n✅ Padrão detectado: Quadrados perfeitos consecutivos!")
        print(f"Fórmula exata: a(n) = ({primeira_raiz} + n - 1)²")

        pos = ler_posicao()
        resultado = (primeira_raiz + pos - 1) ** 2
        print(f"O termo {pos} da sequência é: {resultado}")
        return True

    # 2. Números primos consecutivos.
    if eh_sequencia_de_primos(lista):
        print("\n✅ Padrão detectado: Sequência de números primos consecutivos!")
        print("Representação exata: a(n) = p(k + n - 1),")
        print(f"em que p(k) = {lista[0]} e p(k) é o primo da posição inicial.")
        print("Regra: cada termo é o próximo número primo após o anterior.")
        print("Observação: não há uma fórmula polinomial simples conhecida para os primos.")

        pos = ler_posicao()
        resultado = lista[-1]

        if pos <= len(lista):
            resultado = lista[pos - 1]
        else:
            for _ in range(pos - len(lista)):
                resultado = proximo_primo(resultado)

        print(f"O termo {pos} da sequência é: {resultado}")
        return True

    # 3. Sequência linear.
    diffs = [lista[i + 1] - lista[i] for i in range(len(lista) - 1)]

    if all(d == diffs[0] for d in diffs):
        razao = diffs[0]
        primeiro = lista[0]
        print("\n✅ Padrão detectado: Sequência Linear!")
        print(f"Fórmula exata: a(n) = {primeiro} + (n - 1) × ({razao})")

        pos = ler_posicao()
        resultado = primeiro + (pos - 1) * razao
        print(f"O termo {pos} da sequência é: {resultado}")
        return True

    # 4. Sequência de 2º grau.
    if len(lista) >= 3:
        segunda_diff = [
            diffs[i + 1] - diffs[i]
            for i in range(len(diffs) - 1)
        ]

        if all(sd == segunda_diff[0] for sd in segunda_diff):
            primeiro = lista[0]
            primeira_diff = diffs[0]
            segunda = segunda_diff[0]

            print("\n✅ Padrão detectado: Sequência de 2º Grau!")
            print("Fórmula exata:")
            print(
                f"a(n) = {primeiro} + (n - 1) × ({primeira_diff}) "
                f"+ ((n - 1)(n - 2) × ({segunda})) / 2"
            )

            pos = ler_posicao()
            resultado = (
                primeiro
                + (pos - 1) * primeira_diff
                + ((pos - 1) * (pos - 2) * segunda) // 2
            )

            print(f"O termo {pos} da sequência é: {resultado}")
            return True

    print("\n❌ Não consegui identificar um padrão conhecido nessa lista.")
    return False


def descobrir_padrao():
    print("v1.3.0")
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
