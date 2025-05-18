
<div align="center">

<h1>Verificador de Equilibrio de Móviles</h1>

</div>

Este proyecto implementa un programa en C# que lee la descripción de varios móviles (estructuras físicas usadas en física básica) y determina si cada uno está en equilibrio o no.

---

## ¿Qué es un móvil?

Un **móvil** es una estructura colgante compuesta por pesos a la izquierda y derecha de una barra. La condición para que esté en equilibrio es:
pi × di = pd × dd

Donde:
- `pi`: peso izquierdo
- `di`: distancia desde el centro hacia el peso izquierdo
- `pd`: peso derecho
- `dd`: distancia desde el centro hacia el peso derecho

Además, tanto `pi` como `pd` pueden ser `0`, lo que significa que en lugar de un peso hay otro **submóvil** anidado en ese lado.

---

## 🚀 ¿Qué hace el programa?

- Lee múltiples casos de prueba desde la entrada estándar.
- Cada caso describe un móvil con posible anidamiento de submóviles.
- Evalúa recursivamente si el móvil está equilibrado.
- Imprime `SI` si está en equilibrio, `NO` en caso contrario.
- Finaliza cuando se introduce la línea `0 0 0 0`.

---

## 📄 Formato de entrada

Cada línea tiene el formato: pi di pd dd

```
Ejemplo: 
0 2 0 4
0 3 0 1
1 1 1 1
2 4 2 4
0 0 0 0
``` 
---

## ✅ Ejemplo de salida

Para la entrada anterior, el programa imprimiría:
SI 
NO

## Resumen de trabajo del código
Se lee móviles anidados de forma recursiva, evaluando desde las hojas (pesos simples) hasta el móvil principal. Cada vez que detecta un submóvil (cuando pi == 0 o pd == 0), se llama a sí misma para calcular el peso y el balance de ese submóvil. Luego, aplica la regla de equilibrio para determinar si el conjunto está balanceado.

