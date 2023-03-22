import matplotlib.pyplot as plt

# Построение графика
def graphCreater(x, y):

    plt.figure(label="Изменение линейной сложности в зависимости от количества элементов")

    plt.xlabel("Количество элементов")
    plt.ylabel("Линейная сложность")
    plt.plot(x, y, mec="b")

    plt.legend()
    plt.grid(True)
    plt.show()
