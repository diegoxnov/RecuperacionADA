import numpy as np
from math import ceil, log2
import matplotlib.pyplot as plt
import time
import random

def next_power_of_2(n):
    return 2 ** ceil(log2(n))

def fft(a):
    n = len(a)
    if n == 1:
        return a

    a_even = fft(a[0::2])
    a_odd = fft(a[1::2])

    factor = np.exp(-2j * np.pi / n)
    omega = 1

    y = [0] * n
    for k in range(n // 2):
        y[k] = a_even[k] + omega * a_odd[k]
        y[k + n // 2] = a_even[k] - omega * a_odd[k]
        omega *= factor

    return y

def ifft(a):
    n = len(a)
    a = [x.conjugate() for x in a]
    y = fft(a)
    return [x.conjugate() / n for x in y]

def multiply_integers_fft(a, b):
    a_digits = [int(d) for d in str(a)]
    b_digits = [int(d) for d in str(b)]

    n = len(a_digits) + len(b_digits)
    size = next_power_of_2(n)

    a_padded = a_digits + [0] * (size - len(a_digits))
    b_padded = b_digits + [0] * (size - len(b_digits))

    a_fft = fft(a_padded)
    b_fft = fft(b_padded)

    c_fft = [a_fft[i] * b_fft[i] for i in range(size)]
    c = ifft(c_fft)

    c_real = [round(x.real) for x in c]

    result = 0
    carry = 0
    for i in range(size - 1, -1, -1):
        c_real[i] += carry
        carry = c_real[i] // 10
        c_real[i] %= 10
        result = result * 10 + c_real[i]

    if carry > 0:
        result = carry * (10 ** size) + result

    return result

def harvey_van_der_hoeven(a, b):
    if a < 1000 or b < 1000:
        return a * b
    return multiply_integers_fft(a, b)

def generar_pruebas():
    longitudes = list(range(10, 1001, 100)) # desde 10 hasta 1000 dígitos, de 100 en 100
    tiempos = []

    for l in longitudes:
        a = random.randint(10**(l-1), 10**l - 1)
        b = random.randint(10**(l-1), 10**l - 1)

        start = time.perf_counter()
        harvey_van_der_hoeven(a, b)
        end = time.perf_counter()

        tiempo = end - start
        tiempos.append(tiempo)
        print(f"{l} dígitos: {tiempo:.6f} segundos")

    return longitudes, tiempos

def graficar_resultados(longitudes, tiempos):
    plt.figure(figsize=(10, 6))
    plt.plot(longitudes, tiempos, marker='o', linestyle='-', color='blue')
    plt.title("Tiempo de multiplicación")
    plt.xlabel("Número de dígitos por número")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafico_tiempo")
    plt.show()

if __name__ == "__main__":
    longitudes, tiempos = generar_pruebas()
    graficar_resultados(longitudes, tiempos)
