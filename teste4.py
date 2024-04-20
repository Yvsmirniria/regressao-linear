import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

# Calcular os valores previstos de y com base em diferentes valores de xx
def regressao_linear(x, a1, a2):
    return a1 + a2 * x

# Função para calcular os coeficientes usando o método dos mínimos quadrados
def calcular_coeficientes_minimos_quadrados(x, y):
    N = len(x)
    V = np.column_stack((np.sin(np.pi * np.array(x)), np.cos(np.pi * np.array(x))))
    a = inv(V.T @ V) @ V.T @ y
    return a

def main():
    sair = str
    manterTamanhoVetor = False
    bla = str

    while sair != 'q':
        # Input do usuário para x
        if not manterTamanhoVetor:
            num_points = int(input("Quantidade de elementos do vetor: "))

        x = []
        print("Digite os valores de x:")
        for i in range(num_points):
            x_value = float(input(f"x[{i + 1}]: "))
            x.append(x_value)

        # Input do usuário para y
        y = []
        print("Digite os valores de y:")
        for i in range(num_points):
            y_value = float(input(f"y[{i + 1}]: "))
            y.append(y_value)

        # Calculos da Regressão Linear
        N = len(x)
        ssx = np.sum(np.square(x))
        sx = np.sum(x)
        sxy = np.sum(np.multiply(x, y))
        sy = np.sum(y)

        a1 = (ssx * sy - sx * sxy) / (N * ssx - sx * sx)
        a2 = (N * sxy - sx * sy) / (N * ssx - sx * sx)

        # Exibir os resultados da RL
        print("Resultado da Regressão Linear:")
        print("a1:", a1)
        print("a2:", a2)

        # Gerar os pontos para a linha de regressão
        xx = np.linspace(-1.3, 1.23, 100)

        calcular_regressao_linear = input("\nCalcular com regressão linear (AJUSTE LINEAR GERAL simples? (s/n)): ")
        calcular_com_minimos_quadrados = input("Deseja calcular os coeficientes usando mínimos quadrados? (s/n): ").lower()

        plt.plot(x, y, 'ro', label='Dados')
        if calcular_regressao_linear == 's': 
            # Plot dos dados e a linha de regressão
            plt.plot(xx, regressao_linear(xx, a1, a2), 'b-', label='Linha de regressão')

        if calcular_com_minimos_quadrados == 's':
            # Calcular os coeficientes usando a fórmula dos mínimos quadrados específica
            coeficientes_minimos_quadrados = calcular_coeficientes_minimos_quadrados(x, y)
            print("Coeficientes calculados usando mínimos quadrados com a fórmula específica:")
            print("a0:", coeficientes_minimos_quadrados[0])
            print("a1:", coeficientes_minimos_quadrados[1])
            y_pred = np.sin(np.pi * np.array(xx)) * coeficientes_minimos_quadrados[0] + np.cos(np.pi * np.array(xx)) * coeficientes_minimos_quadrados[1]
            plt.plot(xx, y_pred, 'b-', label='Linha de regressão específica')

            
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

        sair = input("Digite 'q' para sair ou pressione Enter para continuar: ")

        if sair != 'q':
            if not manterTamanhoVetor:
                bla = input("Manter o tamanho do vetor igual para todas as operações? (s/n): ").lower()
                if bla == 's':
                    manterTamanhoVetor = True
                else:
                    manterTamanhoVetor = False

if __name__ == "__main__":
    main()
