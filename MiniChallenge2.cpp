/*Dia 8 - Suma de numeros en C++
Escribir un programa que pida al usuario dos números y los sume*/

#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int valor1 , valor2 ;
    cout << "Inserte primer numero: ";
    cin >> valor1;
    cout << "Inserte segundo valor: ";
    cin >> valor2;
    int suma = valor1 + valor2;
    cout << "La suma de " << valor1 << "+" << valor2 << " = " << suma << endl;
    return 0;
}

