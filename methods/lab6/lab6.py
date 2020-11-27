import numpy as np
from scipy import integrate

START_X = 0
END_X = 0.9

# sqrt(asin(x)/(1-x^2)); №1083
def f(x: np):
    return np.sqrt(np.arcsin(x) / (1 - x**2))


methods_error = [[], [], []]
for x1, x2 in [(0, 0.9), (0.1, 0.8), (0.1, 0.5), (0, 0.1)]:
    START_X, END_X = x1, x2
    print("Отрезок: [{}, {}]".format(START_X, END_X))
    x = np.linspace(START_X, END_X, num=7)
    res = [integrate.trapz(f(x), x), integrate.simps(f(x), x), integrate.fixed_quad(f, START_X, END_X, n=5)[0]]
    best_res, error = integrate.quad(f, START_X, END_X)
    print("Трапеции, 6 промежутков: {};".format(res[0]))
    print("Симпсон, 6 промежутков:  {};".format(res[1]))
    print("Гаусс, 5 узлов: {};".format(res[2]))
    print("Лучшее: {}; Ошибка: {};\n".format(best_res, error))
    for i in range(3):
        methods_error[i] += [abs(abs(res[i] - best_res) - error)]

print("Стандартное отклонение для трапеции, Симпсона и Гаусса:")
print([np.std(error_arr) for error_arr in methods_error])
