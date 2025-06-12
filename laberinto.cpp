#include <iostream>
#include <vector>
#include <stdlib.h> //Permite usar el New y el Delete
#include <random>
using namespace std;

int filas;
int columnas;
string bloque = "⬛️";
string pasillo = "⬜️";
string **tablero;
vector<vector<bool>> visitados;

void crearTablero();
void mostrarTablero();
void liberarTablero();
void crearLaberinto(int x, int y);
bool resolverTablero(int x, int y);
void mostrarVisitados();
int main()
{  
    cout << "Ingrese cantidad de filas: "<< endl;
    cin >> filas;
    cout << "Ingrese cantidad de columnas: " << endl;
    cin >> columnas;
    //Si las filas y columnas son pares, las tranformamos en impares para mantener los muros externos
    if (filas %2 == 0 && columnas %2 == 0){
        filas += 1;
        columnas += 1;
    }
   crearTablero();
   visitados = vector<vector<bool>>(filas, vector<bool>(columnas, false));
   crearLaberinto(1,1);
   mostrarTablero();
   visitados = vector<vector<bool>>(filas, vector<bool>(columnas, false));
   resolverTablero(1,1);
   cout << endl;
   mostrarTablero();
   liberarTablero();
   cout << endl;
   mostrarVisitados();
    return 0;
}

void crearTablero(){
    tablero = new string*[filas];
    for(int i = 0; i<filas; i++){
        tablero[i] = new string[columnas];
    }
    for(int i =0;i<filas;i++){
        for (int j = 0; j < columnas; j++)
        {
            tablero[i][j] = bloque;
        }
        
    }
    
}
void mostrarTablero(){

    for(int i =0;i<filas;i++){
        for (int j = 0; j < columnas; j++)
        {
            cout << tablero[i][j]<< " ";

        }
        cout << endl;
    }
}
void liberarTablero() {
    // Liberar la memoria del tablero
    for (int i = 0; i < filas; i++) {
        delete[] tablero[i]; // Liberar cada fila
    }
    delete[] tablero; // Liberar el arreglo de punteros
}
void crearLaberinto(int x,int y){
    vector<pair<int, int>> direcciones = {
        {2, 0},   // abajo
        {-2, 0},  // arriba
        {0, 2},   // derecha
        {0, -2}   // izquierda
    };

    // Barajar direcciones aleatoriamente
    random_device rd;//Pide una valor 'semilla' al sistema
    mt19937 g(rd()); 
    shuffle(direcciones.begin(), direcciones.end(), g);//mezcla las direcciones para que tener aleatoriedad 
    visitados[x][y] = true;
    tablero[x][y] = pasillo;//Crea el pasillo 
    for (auto dir : direcciones){
        int nx = x + dir.first ;
        int ny = y + dir.second ;
       

    if((nx > 0 && nx <= filas-1) && (ny > 0 && ny <= columnas-1) && !visitados[nx][ny]){
        tablero[x + dir.first/2][y + dir.second/2] = pasillo;
        crearLaberinto(nx,ny);
     }
    }
}
bool resolverTablero(int x,int y){
    
    vector<pair<int, int>> direcciones = {
        {1, 0},   // abajo
        {-1, 0},  // arriba
        {0, 1},   // derecha
        {0, -1}   // izquierda
    };
    if (x < 0 || x >= filas || y < 0 || y >= columnas)
        return false;
    // Evalua si la posicion es la salida
    if(x == filas -2 && y == columnas -2){
        tablero[x][y] = "🟧";
        return true;
    }
    // Evalua si la posicion es un muro
    if(tablero[x][y] == "⬛️" || visitados[x][y]){
        return false;
    }
    // modifica la posicion de false a true
    visitados[x][y] = true;
    //recorre las direcciones y suma a la posicion 
    for(auto direccion : direcciones){
        int nx = x + direccion.first;
        int ny = y + direccion.second;
        //llama a recursividad 
        if(resolverTablero(nx,ny)){
            tablero[x][y] = "🟧";
            return true;
        }


    }
    return false;
}
//Funcion que imprime el tablero con los valores boobleanos de cada posicion
void mostrarVisitados(){
    for(int i =0;i<filas;i++){
        for (int j = 0; j < columnas; j++)
        {
            cout << visitados[i][j]<< " ";

        }
        cout << endl;
    }
    
}