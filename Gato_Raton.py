import os
from copy import deepcopy
#Funcion que recibe el input del Usuario y verifica que este entre las teclas validad
def movimiento_valido(movimiento,juego):
    while True:
        if movimiento in ['w','s','d','a','r']:# Si el input esta entre las teclas validas de retorna
            return movimiento
        if movimiento in ['q','e','c','z'] and juego.habilitar_poder: #Una vez que el switch 'habilitar_poder' cambie a True se consideraran los movimientos diagonales
            return movimiento
        else:
            print('Arriba --- "w" \n Abajo ---"s" \n Derecha --- "d"\n Izquierda --- "a"\n Si consigues comer el queso (🧀) puedes realizar los movimientos en diagonal con "q","e","c","z"\n')
            movimiento = input('Ingrese Movimiento valido:')
#Clase del gato que contiene sus caracteristicas
class Gato():
    def __init__(self):
        self.personaje = '🐱'
        self.fila_actual, self.columna_actual = 4,5
#Clase del Raton que contiene sus caracteristicas        
class Raton():
    def __init__(self):
      self.personaje = '🐭'
      self.fila_actual = 1
      self.columna_actual = 1
#Clase del Tablero donde se establecen las dimensiones y si colocan los obstaculos
class Tablero():
    def __init__(self):
      self.columnas_tablero = 10
      self.filas_tablero = 10
      self.casilla_vacia = '⬜'
      self.casilla_de_queso = '🧀'
      self.fila_queso,self.columna_queso = 2,7
      self.fila_escape,self.columna_escape = 7,5
      self.casilla_de_escape = '🚪'
      self.casillas_obstaculos= [(7,6),(6,6),(2,2),(2,3),(3,2),(3,3),(3,6),(6,5),(6,4),(6,3)]
      self.obstaculo = '🟧'
      self.tablero = [['⬜️' for _ in range(self.columnas_tablero)] for _ in range(self.filas_tablero)]     
      for columnas in range(self.columnas_tablero):
          fila_inf,columna_inf = self.filas_tablero-1,columnas
          fila_sup,columna_sup = 0,columnas
          self.casillas_obstaculos.append((fila_inf,columna_inf))
          self.casillas_obstaculos.append((fila_sup,columna_sup))
      for filas in range(self.filas_tablero):
          fila_inf,columna_inf = filas,self.columnas_tablero-1
          fila_sup,columna_sup = filas,0
          self.casillas_obstaculos.append((fila_inf,columna_inf))
          self.casillas_obstaculos.append((fila_sup,columna_sup))
      for fila,columna in self.casillas_obstaculos:
          self.tablero[fila][columna] = self.obstaculo
          
      self.tablero[self.fila_escape][self.columna_escape] = self.casilla_de_escape
      self.tablero[self.fila_queso][self.columna_queso] = self.casilla_de_queso

    def mostrar_tablero(self):
       os.system('cls' if os.name == 'nt' else 'clear') #LIMPIA EL TERMINAL PERMITIENDONOS TENER SOLO UN TABLERO 
       for fila in self.tablero:
         print(' '.join(fila))
#Clase del juego donde de realizan todas la funciones basicas del programa            
class Juego():
   def __init__(self,jugador,maquina):
      self.tab = Tablero()
      self.jugador = jugador
      self.maquina = maquina
      self.maquina_personaje = self.maquina.personaje
      self.habilitar_poder = False
      self.queso = self.tab.casilla_de_queso
      self.fila_jugador , self.columna_jugador = self.jugador.fila_actual, self.jugador.columna_actual
      self.fila_maquina , self.columna_maquina = self.maquina.fila_actual, self.maquina.columna_actual
      self.tab.tablero[self.fila_jugador][self.columna_jugador] = self.jugador.personaje
      self.tab.tablero[self.fila_maquina][self.columna_maquina] = self.maquina.personaje
   def hacer_movimiento_jugador(self,movimiento):
      nueva_fila,nueva_columna = self.fila_jugador,self.columna_jugador
        #Subir
      if self.fila_jugador > 0 and movimiento == 'w':
            nueva_fila -= 1
        #Bajar
      elif self.fila_jugador < (self.tab.filas_tablero - 1) and movimiento == 's':
            nueva_fila += 1
        #Derecha
      elif self.columna_jugador < (self.tab.columnas_tablero -1) and movimiento == 'd':
            nueva_columna += 1
        #Izquierda
      elif self.columna_jugador > 0 and movimiento == 'a':
            nueva_columna -= 1
      #Si el raton come el queso, el switch "habilitar_poder" cambia a True, habilitando los movimientos en diagonales
      if self.fila_jugador == self.tab.fila_queso and self.columna_jugador == self.tab.columna_queso:
          self.habilitar_poder = True
          self.tab.tablero[self.tab.fila_queso][self.tab.columna_queso] = self.tab.casilla_vacia
      #Bloque que realiza los movimientos diagonales
      if self.habilitar_poder and movimiento in ['e', 'q', 'c', 'z']:
        if movimiento == 'e' and self.fila_jugador > 0 and self.columna_jugador < self.tab.columnas_tablero - 1:
          nueva_fila -= 1
          nueva_columna += 1
        elif movimiento == 'q' and self.fila_jugador > 0 and self.columna_jugador > 0:
          nueva_fila -= 1
          nueva_columna -= 1
        elif movimiento == 'c' and self.fila_jugador < self.tab.filas_tablero - 1 and self.columna_jugador < self.tab.columnas_tablero - 1:
          nueva_fila += 1
          nueva_columna += 1
        elif movimiento == 'z' and self.fila_jugador < self.tab.filas_tablero - 1 and self.columna_jugador > 0:
          nueva_fila += 1
          nueva_columna -= 1
          #Evalua que la nueva posicion no sea igual a la anterios y realiza el movimiento dependiendo del caso
      if (nueva_fila,nueva_columna) != (self.fila_jugador,self.columna_jugador) and (nueva_fila,nueva_columna) not in self.tab.casillas_obstaculos:
        #Permite que el caracter de la casilla de escape sea inmutable en el tablero
        if nueva_fila == self.tab.fila_escape and nueva_columna == self.tab.columna_escape:
            self.tab.tablero[nueva_fila][nueva_columna] = self.tab.casilla_de_escape
            self.tab.tablero[self.fila_jugador][self.columna_jugador] = self.tab.casilla_vacia
            self.fila_jugador,self.columna_jugador = nueva_fila,nueva_columna
        #Si el raton llega a las fila de escape hace que el caracter del raton desaparezca y quede el de la casilla de escape
        
        elif self.fila_jugador == self.tab.fila_escape and self.columna_jugador == self.tab.columna_escape:
            self.tab.tablero[self.fila_jugador][self.columna_jugador] = self.tab.casilla_de_escape
            self.tab.tablero[nueva_fila][nueva_columna] = self.jugador.personaje
            self.fila_jugador,self.columna_jugador = nueva_fila,nueva_columna
        #Si solo es un movimiento del raton cualquiera, se limpia la casilla anterios y se coloca el caracter del raton en la nueva posicion    
        else:
            self.tab.tablero[nueva_fila][nueva_columna] = self.jugador.personaje
            self.tab.tablero[self.fila_jugador][self.columna_jugador] = self.tab.casilla_vacia
            self.fila_jugador,self.columna_jugador = nueva_fila,nueva_columna


   def jugadas(self,fila,columna,personaje):
       jugadas = []
       # Sube
       if fila > 0:
             jugadas.append((fila - 1,columna))    
        #Baja  
       if fila < (self.tab.filas_tablero - 1):
            jugadas.append((fila + 1,columna))
        #Derecha
       if columna < (self.tab.columnas_tablero-1):
             jugadas.append((fila,columna +1))
        #Izquierda
       if columna > 0:
             jugadas.append((fila,columna -1))
       jugadas_exc = [coordenadas for coordenadas in jugadas if coordenadas not in self.tab.casillas_obstaculos]
       return jugadas_exc
   def juego_termina(self):
           #Usando el switch "habilitar_poder" nos aseguramos que el raton coma el queso primeramente antes de poder escapar
           if self.habilitar_poder:
             if self.fila_jugador == self.tab.fila_escape and self.columna_jugador == self.tab.columna_escape:
                return -100
           elif self.fila_jugador == self.fila_maquina and self.columna_jugador == self.columna_maquina:
               return  100
           return None
#Clase minimax donde esta toda la logica para que la maquina piense
class Minimax():
    #Dentro del bloque de codigo se hace uso de self.juego.tab.tablero para acceder al tablero debido a que de esta manera los cambios realizados se podran ver reflejados en el tablero
    def __init__(self,juego):
        self.juego = juego
        self.personaje_jugador = self.juego.jugador.personaje
        self.personaje_maquina = self.juego.maquina.personaje
        self.casilla_vacia = self.juego.tab.casilla_vacia
        self.fila_jugador ,self.columna_jugador = self.juego.fila_jugador , self.juego.columna_jugador
        self.fila_maquina , self.columna_maquina = self.juego.fila_maquina , self.juego.columna_maquina
        self.profundidad = 5
    def minimax(self,profundidad ,es_maximizador,alpha,beta):
        ganador = self.juego.juego_termina() #usa el modulo juego.termina() para determinar si hay un ganador
        if ganador is not None:
            return ganador
        
        elif profundidad == 0:
            distancia_gato_raton = abs(self.juego.fila_jugador - self.juego.fila_maquina) + abs(self.juego.columna_maquina - self.juego.columna_jugador)
            return -distancia_gato_raton if es_maximizador else distancia_gato_raton
        if es_maximizador:
            mejor_puntuacion = -float('inf')
            for fila,columna in self.juego.jugadas(self.juego.fila_maquina,self.juego.columna_maquina,self.personaje_maquina):
             #Copia Actual
             tablero_ant = deepcopy(self.juego.tab.tablero)
             fila_ant,columna_ant = self.juego.fila_maquina,self.juego.columna_maquina
             #Movimiento
             self.juego.tab.tablero[self.juego.fila_maquina][self.juego.columna_maquina] = self.casilla_vacia
             self.juego.tab.tablero[fila][columna]= self.personaje_maquina
             self.juego.fila_maquina,self.juego.columna_maquina = fila,columna
             #Evalua
             puntuacion = self.minimax(profundidad-1,False,alpha,beta)
             #Restaura
             self.juego.tab.tablero = tablero_ant
             self.juego.fila_maquina,self.juego.columna_maquina = fila_ant,columna_ant
             mejor_puntuacion = max(mejor_puntuacion,puntuacion)
             #Evalua la Poda. Si el valor de Beta no puede superar o igualar el valor de Alpha entonces se descarta
             alpha = max(alpha,mejor_puntuacion)
             if alpha >= beta:
                break 
            return mejor_puntuacion
        else:
          mejor_puntuacion = float('inf')
          for fila,columna in self.juego.jugadas(self.juego.fila_jugador,self.juego.columna_jugador,self.personaje_jugador):
             #Copia Actual
             tablero_ant = deepcopy(self.juego.tab.tablero)
             fila_ant,columna_ant = self.juego.fila_jugador,self.juego.columna_jugador
             #Movimiento
             self.juego.tab.tablero[self.juego.fila_jugador][self.juego.columna_jugador] = self.casilla_vacia
             self.juego.tab.tablero[fila][columna]= self.personaje_jugador
             self.juego.fila_jugador,self.juego.columna_jugador = fila ,columna
             #Evalua
             puntuacion = self.minimax(profundidad-1,True,alpha,beta)
             #Restaura
             self.juego.tab.tablero = tablero_ant
             self.juego.fila_jugador,self.juego.columna_jugador = fila_ant,columna_ant
             mejor_puntuacion = min(mejor_puntuacion,puntuacion)
             #Evalua la Poda
             beta = min(beta,mejor_puntuacion)
             if alpha >= beta:
                break
          return mejor_puntuacion
    def mejor_jugada(self):
       alpha = -float('inf')
       beta = float('inf')
       mejor_puntuacion = -float('inf')
       mejor_jugada = None
       for fila,columna in self.juego.jugadas(self.juego.fila_maquina,self.juego.columna_maquina,self.personaje_maquina):
            #Se guarda el estado actual
            tablero_ant = deepcopy(self.juego.tab.tablero)
            fila_ant,columna_ant = self.juego.fila_maquina,self.juego.columna_maquina
            #Se realiza el movimiento
            self.juego.tab.tablero[self.juego.fila_maquina][self.juego.columna_maquina] = self.casilla_vacia
            self.juego.tab.tablero[fila][columna]= self.personaje_maquina
            self.juego.fila_maquina,self.juego.columna_maquina = fila,columna
            #Se evalua si es un movimiento terminal
            if self.juego.fila_maquina == self.juego.fila_jugador and self.juego.columna_maquina == self.juego.columna_jugador:
               mejor_jugada = (fila,columna)
               return mejor_jugada
            #Se envia al minimax
            puntuacion = self.minimax(self.profundidad,False,alpha,beta)
            #Se regresa al estado actual
            self.juego.tab.tablero = tablero_ant
            self.juego.fila_maquina,self.juego.columna_maquina = fila_ant,columna_ant
            if puntuacion > mejor_puntuacion:
               mejor_puntuacion = puntuacion
               mejor_jugada = (fila,columna)
       return mejor_jugada
    def mover_maquina(self):
      jugada = self.mejor_jugada()
      if jugada:
        fila, columna = jugada
        self.juego.tab.tablero[self.juego.fila_maquina][self.juego.columna_maquina] = self.casilla_vacia
        self.juego.tab.tablero[fila][columna] = self.personaje_maquina
        self.juego.fila_maquina, self.juego.columna_maquina = fila, columna


       
#INICIO DEL PROGRAMA    
   
#Se crean las instancias a usarse
jugador = Raton() 
maquina = Gato() 
juego = Juego(jugador,maquina) 
minimax = Minimax(juego) 

while True:
  juego.tab.mostrar_tablero() #Mostramos el tablero 
  print('Arriba --- "w" \n Abajo ---"s" \n Derecha --- "d"\n Izquierda --- "a"\n Consigue comer el queso (🧀) para realizar los movimientos en diagonal con "q","e","c","z" y poder llegar a la salida\n')
  movimiento = input("Ingrese movimiento: ")
  movimiento_valido(movimiento,juego) #Enviamos el input a la funcion movimiento_valido para validar el input
  if movimiento == 'r': #Usamos la letra 'r' como escape del juego
     break
  juego.hacer_movimiento_jugador(movimiento) #modulo que realiza el movimiento del jugador
  estado_de_juego = juego.juego_termina() #Evalua si el juego ya paso por un caso terminal "Gato come raton o Raton come queso"
  if estado_de_juego == -100: #Si gana el jugador
     #Mostramos el ultimo estado del tablero
     juego.tab.mostrar_tablero()
     print("Ganaste")
     break
  elif estado_de_juego == 100: #Si gana la maquina
     #Mostramos el ultimo estado del tablero
     juego.tab.mostrar_tablero()
     print("Te atrapo el gato")
     break   
  minimax.mover_maquina() # Modulo que hace el movimineto de la maquina 
  # Luego de que la maquina realice su movimiento, se evalua si se llego a un estado terminal, si no , se vuelve al inicio del bucle
  estado_de_juego = juego.juego_termina()
  if estado_de_juego == -100:
        juego.tab.mostrar_tablero()
        print("Ganaste")
        break
  elif estado_de_juego == 100:
        juego.tab.mostrar_tablero()
        print("Te atrapó el gato")
        break
  
