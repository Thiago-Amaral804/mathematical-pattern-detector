def descobrir_padrao():
    print("v1.1.1")
    print("-- Bah meia noite e eu aq fazendo desafio ;-; --\n")
    
    entrada = input("Digite a lista: ")
    
    try:
        # Ageita o bomba da lista pra caso esteja errada.
        lista = [int(x.strip()) for x in entrada.split(',') if x.strip()]
        
        if len(lista) < 2:
            print("Minimo de 2 números.")
            return

        # 1. Vê se é quadrado perfeito (n²)
        if all(lista[i] == (i + 1) ** 2 for i in range(len(lista))):
            print("\n✅ Padrão detectado: Números ao Quadrado (n²)")
            pos = int(input("Qual posição você quer descobrir? "))
            print(f"O número na posição {pos} é: {pos**2}")
            return

        # 2. Vê se é linear
        diffs = [lista[i+1] - lista[i] for i in range(len(lista)-1)]
        
        if all(d == diffs[0] for d in diffs):
            razao = diffs[0]
            ajuste = lista[0] - razao
            sinal = "+" if ajuste >= 0 else "-"
            print(f"\n✅ Padrão detectado: Sequência Linear!")
            print(f"A fórmula é: {razao}n {sinal} {abs(ajuste)}")
            
            pos = int(input("Qual posição você quer descobrir? "))
            print(f"O número na posição {pos} é: {(razao * pos) + ajuste}")
            return

        # 3. O upgrade brabo: Sequência de 2º Grau
        if len(lista) >= 3:
            # Aqui a gente vê a diferença da diferença, o bagulho é doido kkkkkk (coringando)
            segunda_diff = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
            
            if all(sd == segunda_diff[0] for sd in segunda_diff):
                print("\n✅ Padrão detectado: Sequência de 2º Grau")
                print("Dica: Aumenta de", segunda_diff[0], "em", segunda_diff[0])
                
                pos_alvo = int(input("Qual posição você quer prever? "))
                
                # Grande atualizacão: O pc usa a formula invez de "for" 👍
                a1 = lista[0]
                d1 = diffs[0]
                d2 = segunda_diff[0]
                n = pos_alvo
                
                # Fórmula: a1 + (n-1)d1 + (n-1)(n-2)d2 / 2
                resultado = a1 + (n - 1) * d1 + ((n - 1) * (n - 2) * d2) // 2
                
                print(f"O número na posição {pos_alvo} é: \n\n{resultado}")
                return

        print("\n❌ Padrão muito complexo! Nem o Sherlock deu conta dessa.")

    except ValueError:
        # Tecnica ante idiota.
        print("\n❌ Somente números inteiros separados por vírgula,")

# O código é meio bagunçado, mas é pra ser divertido e fácil de entender.
# (mentira kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk)
if __name__ == "__main__":
    descobrir_padrao()