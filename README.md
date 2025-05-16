
<div align="center">

<h1>Informe de Algoritmo David Harvey y Joris van der Hoeven</h1>


</div>


# Justificación Técnica: Implementación del Algoritmo de Harvey y van der Hoeven en Python

## Introducción

El algoritmo desarrollado por **David Harvey y Joris van der Hoeven** en 2019 representa uno de los avances más importantes en la multiplicación de enteros grandes, al lograr una complejidad de **O(n log n)** utilizando técnicas como transformadas rápidas (FFT/NTT), convoluciones truncadas, optimizaciones numéricas y reconstrucción modular mediante el Teorema Chino del Resto (CRT).

Este algoritmo es altamente eficiente, pero también requiere una implementación matemática y algorítmica compleja, que implica transformadas sobre cuerpos finitos, manejo de enteros de precisión arbitraria, y estructuras numéricas avanzadas.

## Justificación para el uso de Python

Dado el nivel de complejidad requerido por el algoritmo, Python resulta una elección mucho más adecuada por las siguientes razones:

### Disponibilidad de bibliotecas especializadas
- `gmpy2`: permite el uso de enteros de precisión arbitraria con alto rendimiento.
- `numpy`: ofrece herramientas para trabajar con vectores y realizar transformadas rápidas de Fourier (FFT).
- `sympy`: útil para álgebra simbólica y validación matemática.
- Existen implementaciones abiertas de NTT y CRT que pueden ser adaptadas en Python.


# Algoritmo de Harvey y van der Hoeven (HvdH)

## Introducción

El algoritmo de **Harvey y van der Hoeven** (2019) es el primer método que logra una multiplicación de enteros grandes con una complejidad de **O(n log n)** en el modelo de cómputo de Turing. Está basado en:

- Transformadas rápidas (FFT/NTT).
- Convoluciones truncadas.
- Técnicas de reducción modular.
- Reconstrucción mediante el Teorema Chino del Resto (CRT).
- Métodos inspirados en Schönhage-Strassen, pero más optimizados.

---

## Descripción General del Algoritmo

### 1. División de números grandes
Los enteros de entrada se dividen en bloques o "dígitos grandes" que permiten representar el número como un polinomio.

Ejemplo: 
A = a₀ + a₁·B + a₂·B² + ... + aₙ·Bⁿ
B = b₀ + b₁·B + b₂·B² + ... + bₘ·Bᵐ

Donde `B` es la base del bloque (potencia de 2 o 10), y los coeficientes son menores que `B`.

---

### 2. Transformada rápida (NTT)
Se aplica la **NTT (Number Theoretic Transform)** a los coeficientes de los polinomios para transformarlos al dominio de la frecuencia y permitir su multiplicación punto a punto.

Esto evita la multiplicación polinomial directa de O(n²) y la reduce a O(n log n).

---

### 3. Multiplicación en el dominio transformado
Los polinomios transformados se multiplican **elemento a elemento** en el dominio NTT (frecuencia), lo cual es muy eficiente.

---

### 4. Transformada inversa (INTT)
Se aplica la transformada inversa (INTT) para regresar al dominio original y obtener el polinomio resultante.

---

### 5. Reconstrucción del resultado
Se utilizan técnicas como:

- **CRT (Teorema Chino del Resto)** para combinar resultados cuando se trabaja con múltiples primos.
- **Corrección de acarreo (carry propagation)** para convertir el polinomio en un número entero final.

---

## Uso de Librerías en Python

| Etapa                            | Descripción                                                              | Librería recomendada     |
|----------------------------------|---------------------------------------------------------------------------|--------------------------|
| División en bloques              | Conversión de enteros a coeficientes polinomiales                        | `gmpy2`, `int`, propio   |
| Transformada NTT                 | Implementación modular de la FFT en cuerpos finitos                      | `custom`, `numpy`, `sympy` (manual) |
| Multiplicación punto a punto     | Producto de coeficientes en dominio de frecuencia                        | `numpy`, propio          |
| Transformada inversa (INTT)      | NTT inversa para recuperar los coeficientes originales                   | `custom`, `sympy`        |
| Teorema Chino del Resto (CRT)    | Combinar resultados de diferentes módulos para obtener un resultado único | `sympy.ntheory`, propio |
| Corrección de acarreo            | Ajuste del resultado para obtener el número correcto                     | `gmpy2`, `manual`        |

---

## Comparación de Complejidad Algorítmica

| Algoritmo                         | Complejidad Temporal     | Idea Principal                                       |
|----------------------------------|--------------------------|------------------------------------------------------|
| Multiplicación clásica           | O(n²)                    | Multiplicación directa de dígitos                    |
| **Karatsuba**                    | O(n^1.585)               | Divide y vencerás con tres multiplicaciones recursivas |
| **Harvey–van der Hoeven (HvdH)** | **O(n log n)**           | NTT + CRT + truncamiento + optimización numérica     |

---

---

## 🛠️ Limitaciones Prácticas

Aunque el algoritmo de Harvey y van der Hoeven (HvdH) es teóricamente el más rápido conocido para la multiplicación de enteros grandes con complejidad **O(n log n)**, presenta importantes desafíos para su implementación práctica:

- **Complejidad de implementación**: Involucra una combinación sofisticada de transformadas, convoluciones truncadas, CRT, y manejo modular eficiente, lo que lo hace difícil de codificar correctamente y de depurar.
- **Poca ganancia en tamaños pequeños**: Para enteros de tamaños comunes (por ejemplo, cientos o miles de dígitos), otros algoritmos como Karatsuba o Toom-Cook son más rápidos en la práctica.
- **Altos requisitos de precisión modular**: Se requieren primos grandes especiales (Números de Fermat o de Mersenne) para implementar correctamente la NTT, lo cual limita la generalidad del algoritmo.
- **Gestión de acarreo compleja**: Aunque el algoritmo minimiza el acarreo, en la etapa final este sigue siendo un problema no trivial que puede afectar la precisión y el rendimiento.
- **Uso limitado en librerías existentes**: Actualmente, solo bibliotecas muy especializadas (como `GMP` y variantes internas de `mpir`) contemplan aproximaciones a HvdH, y rara vez se usan en sistemas reales por su complejidad.

---

## 🚀 Aplicaciones

El algoritmo de HvdH es especialmente relevante en contextos donde se requiere multiplicación de enteros extremadamente grandes con alta eficiencia:

- **Criptografía de clave pública**: Sistemas como RSA requieren multiplicaciones de enteros de miles a millones de bits.
- **Álgebra computacional**: Software como Mathematica, Maple, y SageMath realiza multiplicaciones simbólicas de alto nivel.
- **Computación científica de alta precisión**: En simulaciones numéricas que requieren precisión arbitraria.
- **Cómputo en teoría de números**: En primalidad, factorización y verificación de conjeturas matemáticas.
- **Cálculo de constantes matemáticas**: Cálculo de millones de dígitos de π, e, etc., que requiere multiplicaciones eficientes.

---

## 🧠 Relevancia del Algoritmo en la Computación Moderna

La contribución de Harvey y van der Hoeven representa un hito teórico en la computación aritmética:

- **Demostración de frontera teórica**: Probar que se puede alcanzar O(n log n) en multiplicación de enteros es un logro fundamental en teoría de algoritmos.
- **Motivación para optimización de librerías**: Inspira mejoras en bibliotecas como GMP, que buscan acercarse a este rendimiento teórico.
- **Interconexión con otras áreas**: El uso de FFTs numéricas y NTTs modulares conecta este algoritmo con el procesamiento de señales, teoría de códigos, álgebra computacional y más.
- **Punto de partida para nuevos algoritmos**: Sirve como base para investigación en algoritmos aún más rápidos o especializados.

En resumen, aunque su uso práctico es limitado por ahora, **la existencia del algoritmo empuja los límites de lo que es posible en computación matemática** y sirve como inspiración para nuevas tecnologías de cómputo de precisión arbitraria.

# 🔍 Análisis detallado del algoritmo de multiplicación usando FFT (inspirado en Harvey & van der Hoeven)

Este documento analiza en detalle la implementación de una versión simplificada del algoritmo de **Harvey y van der Hoeven** para la multiplicación eficiente de números enteros grandes utilizando la **Transformada Rápida de Fourier (FFT)**.

---

## 🧱 Estructura general del código

El algoritmo está organizado en las siguientes partes funcionales:

1. **Cálculo de la siguiente potencia de 2**
2. **Transformada rápida de Fourier (FFT)**
3. **Transformada inversa (IFFT)**
4. **Multiplicación de enteros usando FFT**
5. **Interfaz principal: algoritmo Harvey-Van der Hoeven simplificado**

---

## 📌 Análisis función por función

### Código Desarrollado.

```python
def next_power_of_2(n):
    return 2 ** ceil(log2(n))
```
Encuentra la potencia de 2 más cercana mayor o igual que n.

```python
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

```

Implementación recursiva de la Transformada Rápida de Fourier.
    - Divide el arreglo en partes pares e impares.

    - Aplica FFT recursivamente a cada parte.

    - Combina los resultados usando raíces de la unidad compleja.



```python

def ifft(a):
    n = len(a)
    a = [x.conjugate() for x in a]
    y = fft(a)
    return [x.conjugate() / n for x in y]
```

Transformada inversa de Fourier.
    - Conjuga la entrada.
    - Aplica la FFT.
    - Conjuga la salida y divide entre n.

```python
def multiply_integers_fft(a, b):
    a_digits = [int(digit) for digit in str(a)]
    b_digits = [int(digit) for digit in str(b)]

    n = len(a_digits) + len(b_digits)
    size = next_power_of_2(n)

    a_padded = a_digits + [0] * (size - len(a_digits))
    b_padded = b_digits + [0] * (size - len(b_digits))

    a_fft = fft(a_padded)
    b_fft = fft(b_padded)

    c_fft = [a_fft[i] * b_fft[i] for i in range(size)]
    c = ifft(c_fft)

    c_real = [round(c[i].real) for i in range(size)]

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

```

Multiplica dos enteros grandes usando FFT.

Pasos que sigue este parte de código:
1. Convertir enteros en listas de dígitos

2. Convierte a = 123 en [1, 2, 3]

3. Rellenar con ceros a la siguiente potencia de 2

4. Calcular la FFT de ambos operandos

5. Multiplicación punto a punto en el dominio de la frecuencia

6. Transformada inversa para volver al dominio original

7. Manejo de acarreos para reconstruir el número final

```python
def harvey_van_der_hoeven(a, b):
    if a < 1000 or b < 1000:
        return a * b
    
    return multiply_integers_fft(a, b)
```
Interfaz principal del algoritmo.
- Para números pequeños (menores a 1000), usa la multiplicación estándar (más rápida).

Para enteros grandes, usa multiply_integers_fft, simulando el algoritmo de Harvey y van der Hoeven.



## Conclusión 

El algoritmo de Harvey y van der Hoeven representa el estado del arte en multiplicación entera teórica. Aunque su implementación es compleja, Python ofrece un entorno ideal para desarrollar una versión experimental con el apoyo de librerías como `gmpy2`, `numpy` y `sympy`.

En comparación con otros métodos como Karatsuba y la multiplicación clásica, HvdH es significativamente más rápido en teoría, especialmente para números extremadamente grandes (millones de dígitos).

---

## Referencias

- Harvey, D., & van der Hoeven, J. (2019). Integer multiplication in time O(n log n). *Annals of Mathematics*, 193(2), 563–617.
- https://arxiv.org/abs/1812.03823
- https://gmplib.org
- https://docs.sympy.org





