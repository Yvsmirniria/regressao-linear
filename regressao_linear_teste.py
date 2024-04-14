import numpy as np
import matplotlib.pyplot as plt

#calcular os valores previstos de y com base em diferentes valores de xx
def regressao_linear(x, a1, a2):
    return a1 + a2 * x

def main():

    sair = str
    manterTamanhoVetor = False
    bla = str

    while sair != 'q':
        # Input do usuario para x
        if not manterTamanhoVetor:
            num_points = int(input("Quantidade de elementos do vetor: "))

        x = []
        print("Digite os valores de x:")
        for i in range(num_points):
            x_value = float(input(f"x[{i + 1}]: "))
            x.append(x_value)

        # Input do usuario para y
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

        # Plot dos dados e a linha de regressão
        plt.plot(x, y, 'ro', label='Dados')
        plt.plot(xx, regressao_linear(xx, a1, a2), 'b-', label='Linha de regressão')
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

        sair = input("Digite 'q' para sair ou pressione Enter para continuar: ")

        if not manterTamanhoVetor:
            bla = input("Manter o tamanho do vetor igual para todas as operações? (s/n): ").lower()
        
        if bla == 's':
            manterTamanhoVetor = True
        else:
             manterTamanhoVetor = False

if __name__ == "__main__":
    main()
