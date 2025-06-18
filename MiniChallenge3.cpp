/*Dia 10 - Palíndromo
Escribir un programa que determine si una cadena de caracteres ingresada
por el usuario es un palíndromo */

#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{   int longitudPalabra;
    int contador = 0;
    string palabra;
    cout << "Ingrese palabra: ";
    cin >> palabra;
    longitudPalabra = palabra.size();/*Se halla la longitud de la palabra*/
    for( int letra=0 ; letra < (longitudPalabra -1)/2 ; letra++){ /*Se recorre hasta la mitad de la palabra por ejemplo: somos -- > se recorre --> s --> o --> m */
        if (palabra[letra] == palabra[longitudPalabra - 1 -letra]){ /*Se empieza a evaluar letra inicial y final y asi sucesivamente hasta llegar a la letra central*/
            contador += 1;
        }

    }
    int valor = (longitudPalabra -1)/2;/*Cantidad de letras que debe tener iguales una palabra palindroma 
    somos --> tiene 5 letras debe tener (5 - 1)/2 letras iguales que equivale a 2 */
    if( contador == valor){
        cout << "La palabra es Palindroma " << endl;
    }
    else{
        cout << "La palabra no es Palindroma ";
    }
    
    return 0;
}
