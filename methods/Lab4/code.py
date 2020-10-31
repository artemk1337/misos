import numpy as np

y = [1.23,-1.66,-3.25,-3.11,6.66,7.8,-0.04]

lagrange_array = np.zeros((7, 7), dtype=np.float16)


def lagrange(x, start):
    
    for i in range(0, 7):
        tmp = [ii - i if ii - i != 0 else x - start - i for ii in range(7)]
        lagrange_array[:, i] = tmp
    
    # print(lagrange_array)
    
    L = np.prod([x - i for i in range(-2, 5)]) * sum([yi/np.prod(lagrange_array[i]) for i, yi in enumerate(y)])
    return L


print('Lagrange | Method 1: f(-1.3)={:.4f}, f(1.75)={:.4f}'.format(lagrange(-1.3, -2), lagrange(1.75, -2)))



def newton(x):
    newton_array = np.zeros((7, 7), dtype=np.float16)
    newton_array[:, 0] = y
    # print(newton_array)
    
    for col in range(1, 7):
        for line in range(1, 7):
            if not newton_array[line, col-1]:
                break
            newton_array[line-1, col] = (newton_array[line, col-1] - newton_array[line-1, col-1]) / col
    
    # print(pd.DataFrame(newton_array))
    
    x_ = [x - i for i in range(-2, 5)]
    res = newton_array[0, 0]
    for col in range(1, 7):
        tmp = 1
        for i in range(col):
            tmp *= x_[i]
        res += tmp * newton_array[0, col]
    return res

print('Newton | Method 2: f(-1.3)={:.4f}, f(1.75)={:.4f}'.format(newton(-1.3), newton(1.75)))
