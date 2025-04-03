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
    ])
```
O código principal executa a simulação variando a carga distribuída _*(q)*_ até que o deslocamento máximo eprmitido seja atingido. Os dados são armazenados durante o processo, para posteriormente análise gráfica.

### **_Resultados e Discussões_**

Os resultados obtidos foram plotados utilizando a biblioteca `plotly`. Gerando um gráfico que representa a relação entre a carga distribuída _*q*_ e o deslocamento máximo _*u3*_, permitindo identificar o ponto em que a esrtutura atinge sua capacidade limite.

```ruby
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=u_max_values,
    y=q_values,
    mode='lines+markers',
    name='Dados',
    line=dict(color='blue'),
    marker=dict(size=8)
))
fig.add_shape(type="line",
              x0=u_max_admissivel, y0=0,
              x1=u_max_admissivel, y1=max(q_values) * 1.1,
              line=dict(color="red", dash="dash"),
              name=f'u_max = {u_max_admissivel}')
fig.update_layout(
    title="Convergência Numérica: Deslocamento u vs. Carga q",
    xaxis_title="Deslocamento máximo u (m)",
    yaxis_title="Carga distribuída q (N/m)",
    template="plotly_white"
)
fig.show()
```
O gráfico obtido demonstra um crescimento quase linear do deslocamento em relação à carga, seguido por uma região onde a não linearidade se torna mais evidente. Como resultado, a carga dsitribuída máxima suportada pela estrutura antes de ultrapassar o limite de deslocamento de 1,0 m foi de aproximadamente 1,63 N/m.

<div align="left"><img src="Tópicos em Engenharia de Estruturas VII/Gráfico Gerado.png" width="400px", height="400px"></div>

Além disso, observa-se que o critério de convergência foi atendido. No entanto, em alguns determinados pontos, o número máximo de iterações foi alcançado antes da convergência, indicando a necessidade de um refinamento na malha ou na solução.

### **_Conclusão_**

O referido projeto demonstrou a aplicabilidade da análise não linear na determinação da capacidade de carga de uma estrutura simples, tal como, a de uma em forma de barra. O uso de um método iterativo permitiu uma resolução diversificada e eficiente, fornecendo dados precisos do deslocamento em função da carga aplicada. A implementação das bibliotecas em Python, demonstrou a eficácia e agilidade da aplicabilidade destas ferramentas na resolução numérica e visualização de resultados complexos. Por fim, a abordagem adotada se alinha às metodologias descritas pelos autores Figueiredo e Serafini (2020), reforçando a importância das técnicas numéricas na engenharia estrutural.

### **_Referência_**

```ruby
Fuina, J. S. METODOS DE CONTROLE DE DEFORMA ̧COES PARA ANALISE NAO-LINEAR DE ESTRUTURAS. Disponível em: <https://repositorio.ufmg.br/bitstream/1843/LMCA-769HM7/1/153.pdf>. Acesso em: 3 abr. 2025.
```
```ruby
Figueiredo, R.; Serafini, M. Análise Não Linear de Estruturas. São Paulo: Editora Engenharia, 2020.
```