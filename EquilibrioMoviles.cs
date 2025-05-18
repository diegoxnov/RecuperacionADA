using System;
using System.Collections.Generic;

class MovilBalanceado
{
    // Función recursiva para leer y procesar un móvil
    static (int pesoTotal, bool balanceado) LeerMovil(Queue<string> input)
    {
        // Leer la línea y dividirla en 4 valores
        string[] datos = input.Dequeue().Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int pi = int.Parse(datos[0]);
        int di = int.Parse(datos[1]);
        int pd = int.Parse(datos[2]);
        int dd = int.Parse(datos[3]);

        int pesoIzq;
        bool balanceadoIzq;

        
        if (pi == 0)
        {
            (pesoIzq, balanceadoIzq) = LeerMovil(input);
        }
        else
        {
            pesoIzq = pi;
            balanceadoIzq = true;
        }

        int pesoDer;
        bool balanceadoDer;

        
        if (pd == 0)
        {
            (pesoDer, balanceadoDer) = LeerMovil(input);
        }
        else
        {
            pesoDer = pd;
            balanceadoDer = true;
        }

        
        bool estaBalanceado = balanceadoIzq && balanceadoDer && (pesoIzq * di == pesoDer * dd);

        
        return (pesoIzq + pesoDer, estaBalanceado);
    }

    static void Main()
    {
        List<string> todasLineas = new List<string>();
        string? linea;

        
        while ((linea = Console.ReadLine()) != null)
        {
            linea = linea.Trim();
            if (linea == "") continue;

            // Si es el fin de entrada
            if (linea.Replace(" ", "") == "0000")
                break;

            todasLineas.Add(linea);
        }

        
        Queue<string> cola = new Queue<string>(todasLineas);

        
        while (cola.Count > 0)
        {
            (int _, bool balanceado) = LeerMovil(cola);
            Console.WriteLine(balanceado ? "SI" : "NO");
        }
    }
}
