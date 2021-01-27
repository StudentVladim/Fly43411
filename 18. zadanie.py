import numpy as np
a = int(input("Введите количество строк: "))
b = int(input("Введите количество столбцов: "))
Array = np.zeros((a, b));
print("Введите элементы матриицы\n")
for i in range(a):
    for j in range(b):
        Array[i, j] = input("Array[" + str(i) + "," + str(j) + "] = ")
print(Array)
sdi = np.sum(np.diagonal(Array))
print("Сумма элементов на главной диагонали: " + str(sdi))
sdi = np.sum(np.diagonal(Array[:, ::-1]))
print("Сумма элементов на побоичной диагонали: " + str(sdi))