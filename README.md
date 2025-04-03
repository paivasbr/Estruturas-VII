## **_Análise não Linear Física de uma Estrutura em Forma de Barra_**

- **_Aluna:_** Brenda dos Santos Paiva

**_Disciplina:_** Tópicos em Engenharia de Estruturas VII - Introdução à Análise Não Linear de Estruturas.

### **_Introdução_**

Na engenharia estrutural, um problema é chamado de não-linear quando a rigidez da estrutura muda conforme ela se deforma. Em outras palavras, a resistência da estrutura à deformação não é constante e varia com o deslocamento (Fuina, 2025). Sendo assim, para o desenvolvimento deste estudo implementamos um modelo numérico para avaliação da resposta estrutural de uma barra submetida a um carregamento distribuído crescente. Tendo como objetivo determinar a carga distribuída máxima suportada pela estrutura antes que o deslocamento ultrapasse um valor admissível.

### **_Metodologia_**


 A metodologia empregada considera um sistema de três graus de liberdade e utiliza um método iterativo para a resolução das equações de equilíbrio. Realizando a simulação em Python, utilizando as bibliotecas `numpy` para operações númericas e `plotly` para a visualização dos resultados. A formulação do problema baseia-se na discretização de uma barra com três pontos de deslocamento `(\( u_1, u_2, u_3 \)`. A matriz de rigidez do sistema é definida em função dos deslocamentos, do módulo de elasticidade inicial `\( E_0 \)`, da área da seção transversal `\( S \)` e do comprimento da barra `\( L \)`, conforme apresentado pela função abaixo:

```ruby
 def calcular_matriz_rigidez(u1, u2, u3, E0, S, L, n):
    factor = (2 * E0 * S) / L
    term = n * 2 / L
    return factor * np.array([
        [1, 0, 0],
        [0, 2 - term * (u3 - u1), -1 + term * (u3 - u2)],
        [0, -1 + term * (u3 - u2), 1 - term * (u3 - u2)]
    ]) ```
    
 O código principal executa a simulação variando a carga distribuída _*(q)*_ até que o deslocamento máximo eprmitido seja atingido. Os dados são armazenados durante o processo, para posteriormente análise gráfica.

### **_Resultados e Discussões_**

### **_Conclusão_**

### **_Referência_**

Fuina, J. S. METODOS DE CONTROLE DE DEFORMA ̧COES PARA ANALISE NAO-LINEAR DE ESTRUTURAS. Disponível em: <https://repositorio.ufmg.br/bitstream/1843/LMCA-769HM7/1/153.pdf>. Acesso em: 3 abr. 2025.