import numpy as np

y = [1.23,-1.66,-3.25,-3.11,6.66,7.8,-0.04]

def sum_(y, x):
    x_ = [x - i for i in range(-2, 5)]
    k = [720, -120, 48, -36, 48, -120, 720]
    return sum([y[i]/(x_[i] * k[i]) for i in range(len(k))])

def L(y, x):
    return (x+2)*(x+1)*x*(x-1)*(x-2)*(x-3)*(x-4)*sum_(y, x)

print('Lagrange | Method 1: f(-1.3)={:.4f}, f(1.75)={:.4f}'.format(L(y, -1.3), L(y, 1.75)))




def newton(x):
    newton_array = np.zeros((7, 7), dtype=np.float16)
    newton_array[:, 0] = y
    # print(newton_array)
    
    for col in range(1, 7):
        for line in range(1, 7):
            if not newton_array[line, col-1]:
                break
            newton_array[line-1, col] = (newton_array[line, col-1] - newton_array[line-1, col-1]) / col
    
    # print(newton_array)
    
    x_ = [x - i for i in range(-2, 5)]
    res = newton_array[0, 0]
    for col in range(1, 7):
        tmp = 1
        for i in range(col):
            tmp *= x_[i]
        res += tmp * newton_array[0, col]
    return res

print('Newton | Method 2: f(-1.3)={:.4f}, f(1.75)={:.4f}'.format(newton(-1.3), newton(1.75)))
