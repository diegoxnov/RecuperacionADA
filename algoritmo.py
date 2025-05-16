
import numpy as np
from math import ceil, log2

def next_power_of_2(n):
    """Retorna la siguiente potencia de 2 mayor o igual a n."""
    return 2 ** ceil(log2(n))

def fft(a):
    """Transformada rápida de Fourier (FFT)."""
    n = len(a)
    if n == 1:
        return a
    
    # Dividir en pares e impares
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
    """Transformada inversa rápida de Fourier (IFFT)."""
    n = len(a)
    # Conjugar los valores complejos
    a = [x.conjugate() for x in a]
    
    # Aplicar FFT
    y = fft(a)
    
    # Conjugar el resultado y dividir por n
    return [x.conjugate() / n for x in y]

def multiply_integers_fft(a, b):
    """Multiplicación de enteros usando FFT."""
    # Convertir a lista de dígitos
    a_digits = [int(digit) for digit in str(a)]
    b_digits = [int(digit) for digit in str(b)]
    
    n = len(a_digits) + len(b_digits)
    size = next_power_of_2(n)
    
    # Rellenar con ceros
    a_padded = a_digits + [0] * (size - len(a_digits))
    b_padded = b_digits + [0] * (size - len(b_digits))
    
    # Calcular FFT
    a_fft = fft(a_padded)
    b_fft = fft(b_padded)
    
    # Multiplicación punto a punto en el dominio de frecuencia
    c_fft = [a_fft[i] * b_fft[i] for i in range(size)]
    
    # Transformada inversa
    c = ifft(c_fft)
    
    # Convertir a valores reales y manejar el acarreo
    c_real = [round(c[i].real) for i in range(size)]
    
    # Procesar acarreos
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
    """
    Implementación del algoritmo de Harvey y van der Hoeven para multiplicación rápida
    de enteros grandes usando FFT con complejidad O(n log n).
    
    Esta es una versión simplificada que demuestra el concepto principal.
    Una implementación completa requeriría manejar muchos más detalles
    específicos del algoritmo original.
    """
    # Para números pequeños, usar multiplicación normal
    if a < 1000 or b < 1000:
        return a * b
    
    return multiply_integers_fft(a, b)

# Ejemplo de uso
if __name__ == "__main__":
    a = 12345678901234567890
    b = 98765432109876543210
    
    # Resultado esperado: 1219326311370217952237463801111263526900
    result = harvey_van_der_hoeven(a, b)
    print(f"Multiplicación de {a} × {b} = {result}")
    print(f"Verificación: {a * b}")



