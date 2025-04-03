import numpy as np
import matplotlib.pyplot as plt

def calcular_matriz_rigidez(u1, u2, u3, E0, S, L, n):
    """
    Calcula a matriz de rigidez com base nos deslocamentos e parâmetros do sistema.
    
    Parâmetros:
        u1, u2, u3 (float): Deslocamentos em pontos específicos.
        E0 (float): Módulo de elasticidade.
        S (float): Área da seção transversal.
        L (float): Comprimento da barra.
        n (float): Parâmetro de penalidade.
    
    Retorna:
        numpy.ndarray: Matriz de rigidez calculada.
    """
    factor = (2 * E0 * S) / L
    term = n * 2 / L
    return factor * np.array([
        [1, 0, 0],
        [0, 2 - term * (u3 - u1), -1 + term * (u3 - u2)],
        [0, -1 + term * (u3 - u2), 1 - term * (u3 - u2)]
    ])

def resolver_sistema_iterativo(F, tol, nMaxIterations, E0, S, L, n):
    """
    Resolve o sistema linear de forma iterativa utilizando os critérios de convergência.
    
    Parâmetros:
        F (numpy.ndarray): Vetor de forças.
        tol (float): Tolerância para os critérios de convergência.
        nMaxIterations (int): Número máximo de iterações permitidas.
        E0, S, L, n: Parâmetros para a matriz de rigidez.
    
    Retorna:
        tuple: (u_sol, iteracoes) onde u_sol é o vetor solução e iteracoes é o número
               de iterações realizadas.
    """
    u_sol = np.zeros(3)  # Solução inicial
    
    for i in range(nMaxIterations):
        K = calcular_matriz_rigidez(*u_sol, E0, S, L, n)
        u_novo = np.linalg.solve(K, F)
        res = F - K @ u_novo  # Calcula o resíduo
        
        # Critérios de convergência:
        if np.linalg.norm(res) < tol and np.linalg.norm(u_sol - u_novo) / (np.linalg.norm(u_novo) + 1e-12) < tol:
            return u_novo, i + 1
        
        u_sol = u_novo  # Atualiza a solução para a próxima iteração
    
    print("Aviso: Número máximo de iterações atingido antes da convergência.")
    return u_sol, nMaxIterations

def main():
    # Parâmetros do problema
    E0 = 100000          # Módulo de elasticidade inicial
    S = 1.0              # Área da seção transversal
    L = 100              # Comprimento da barra
    n = 200              # Parâmetro de penalidade
    P = 1                # Força pontual
    u_max_admissivel = 1.0   # Deslocamento máximo permitido (alterado para 1.0)
    tol = 0.001          # Tolerância de convergência
    nMaxIterations = 1000  # Número máximo de iterações
    
    # Inicialização do carregamento distribuído
    q = 0.1              # Valor inicial da carga distribuída
    incremento_q = 0.1   # Incremento para a carga distribuída em cada iteração
    q_max_found = False  # Flag para indicar se a carga máxima foi encontrada
    
    # Listas para armazenar os dados para plotagem
    q_values = []
    u_max_values = []
    
    # Loop para incrementar a carga até atingir o deslocamento máximo permitido
    while not q_max_found:
        # Atualiza o vetor de forças para o valor atual de q
        F = np.array([0, q * L / 2, q * L / 4 + P])
        
        # Resolve o sistema de forma iterativa
        u_sol, iteracoes = resolver_sistema_iterativo(F, tol, nMaxIterations, E0, S, L, n)
        
        # Armazena os resultados para análise
        q_values.append(q)
        u_max_values.append(u_sol[2])
        
        # Critério de parada: se o deslocamento máximo exceder o limite ou se não convergir
        if u_sol[2] > u_max_admissivel or iteracoes == nMaxIterations:
            q_max_found = True
        else:
            q += incremento_q  # Incrementa a carga para a próxima iteração
    
    print(f"Carga distribuída máxima suportada: {q - incremento_q:.3f} N/m, com deslocamento máximo: {u_sol[2]:.3f} m")
    
    # Plot do gráfico de convergência numérica
    plt.figure(figsize=(8, 6))
    plt.plot(u_max_values, q_values, marker='o', linestyle='-')
    plt.axvline(x=u_max_admissivel, color='r', linestyle='--', label=f'u_max = {u_max_admissivel}')
    plt.xlabel('Deslocamento máximo u (m)', fontsize=12)
    plt.ylabel('Carga distribuída q (N/m)', fontsize=12)
    plt.title('Convergência Numérica: Deslocamento u vs. Carga q', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 0.14)
    plt.ylim(0, 2.0)
    plt.show()

if __name__ == "__main__":
    main()
