/*Dia 09 - Ordenamiento de un Array
Escribir un programa que ordene un array de enteros utilizando*/

#include <iostream>
#include <vector>
using namespace std;   
int contador = 0; /*Se inicializa globalmente para usarlo*/       
void ordenanmientoDeunArray(vector<int> &lista){
    int temp =0; /*Variable temporal para guardar un numero */
    int longitud = lista.size();
    for(int i=0; i< longitud-1 ;i++){
        if (lista[i] > lista[i+1]){
          temp = lista[i];/*Se guarda el numero es la variable temporal*/
          lista[i] = lista[i+1]; /*Se intercambian los valores */
          lista[i+1] = temp;
        }
    }
    contador += 1; /* Sube cada llamada recursiva, se debe recorrer toda la lista para terminar el ordenamiento*/
    if(contador == longitud -1 ){ /*Si se recorre toda la lista , se imprimen los valores */
        for(auto n : lista){
            cout << n << endl;
    
        }
    }
    else{ /*Si no , se llama a recursividad*/
        ordenanmientoDeunArray(lista);
    }    
}

int main()
{
    vector<int>lista = {1,3,2,4,7,8,5,6};
    ordenanmientoDeunArray(lista);
    return 0;
}
