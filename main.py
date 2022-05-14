from Algorithm import *

if __name__ == '__main__':
    func = input_func()
    n = input_accuracy()
    res = calculate(func, n)
    print("Результат вычислений:", res)
