import numpy as np
import scipy.integrate as spi


def f(x):
    return x**2


a = 0
b = 2

N = 1_000_000

x_random = np.random.uniform(a, b, N)
integral_mc = (b - a) * np.mean(f(x_random))

print("Інтеграл (Монте-Карло):", integral_mc)

# обчислення:
result_quad, error = spi.quad(f, a, b)

print("Інтеграл (quad):", result_quad)
print("Оцінка похибки quad:", error)
print("Абсолютна похибка:", abs(integral_mc - result_quad))

"""
Інтеграл (quad): 2.666666666666667
Оцінка похибки quad: 2.960594732333751e-14
Абсолютна похибка: 0.003358404808334825
"""
