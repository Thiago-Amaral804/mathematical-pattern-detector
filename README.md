<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Mathematics-Data_Analysis-blueviolet?style=for-the-badge" alt="Math Badge">
  
  <h1>📐 Mathematical Pattern Detector</h1>
  <p align="center">
    <strong>Identificador de sequências numéricas lineares e quadráticas (1º e 2º grau).</strong>
  </p>
</div>

---

## 🧠 Sobre o Detector
Este script analisa uma lista de números fornecida pelo usuário e tenta encontrar o padrão lógico por trás dela. Ele é capaz de identificar:

* **Progressões Aritméticas (1º Grau):** Onde a diferença entre os termos é constante.
* **Sequências de 2º Grau:** Onde a razão da diferença muda de forma constante (funções quadráticas).

## 📊 Como funciona a lógica
O detector utiliza o método das diferenças finitas:
1.  Calcula a primeira diferença entre os termos.
2.  Se não for constante, calcula a segunda diferença.
3.  Gera a fórmula geral da sequência (ex: $a_n = n^2 + n + 1$).

## 🚀 Instruções de Uso

1.  **Execução:**
    ```bash
    python detector.py
    ```
2.  **Entrada:** Insira a sequência separada por espaços ou vírgulas.
3.  **Resultado:** O script retornará o próximo número da sequência e a lei de formação encontrada.

## 📝 Exemplo Prático
> **Entrada:** `2, 6, 12, 20, 30`  
> **Saída:** `Padrão de 2º grau detectado. Próximo termo: 42. Fórmula: n² + n`

---

<div align="center">
  <sub>Ideais para estudantes de matemática, lógica e entusiastas de algoritmos.</sub>
</div>
