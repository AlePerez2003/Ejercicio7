from viajero import Viajero_frecuente
import csv

class Lista_viajero:
    
    def __init__(self):
        self.__viajeros = []
    
    def agregar_viajero(self, unViajero:Viajero_frecuente):
        self.__viajeros.append(unViajero)
        
    def get_viajero(self, num)->Viajero_frecuente:
        return self.__viajeros[num]
    
    def mostrar_viajeros(self):
        for viajero in self.__viajeros:
            viajero.mostrar_datos()
    
    def buscar_viajero(self, num:int):
        i=0
        return_value = -1
        flag = False
        while not flag and i < len(self.__viajeros):
            if self.__viajeros[i].get_numero() == num:
                flag = True
                return_value = i
            else:
                i+=1
        return return_value
        
    def max_millas(self):
        maximo = self.get_viajero(0)
        for viajero in self.__viajeros:
            if viajero > maximo:
                maximo = viajero
        self.mostrar_max(maximo)
        
    def mostrar_max(self, maximo:Viajero_frecuente):
        print('Viajeros con la mayor cantidad de Millas:')
        for viajero in self.__viajeros:
            if viajero.get_millas() == maximo.get_millas():
                viajero.mostrar_datos()

    def test_lista_viajero(self):
        archivo=open('viajeros.csv')
        reader = csv.reader(archivo, delimiter =';')
        for fila in reader:
            numero = int(fila[0])
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millas_acum = int(fila[4])
            Viajero = Viajero_frecuente(numero, dni, nombre, apellido, millas_acum)
            self.__viajeros.append(Viajero)
            
    def mostrar_datos(self):
        for viajero in self.__viajeros:
            print ('Datos del Viajero:')
            print ('Numero: {}'.format(viajero.get_numero()))
            print ('DNI:' + viajero.get_dni())
            print ('Nombre y Apellido:' + viajero.get_nombre() , viajero.get_apellido())
            print ('Millas Acumuladas: {}'.format(viajero.get_millas()))
            print ('')

    def acumular_millas(self, millas:int):
        num = int(input('Ingrese número de viajero'))
        pos = self.buscar_viajero(num)
        viajero = self.get_viajero(pos)
        self.__viajeros[pos] =  millas + viajero
        return
    
    def canjear_millas(self, millas:int):
        num = int(input('Ingrese número de viajero'))
        pos = self.buscar_viajero(num)
        viajero = self.get_viajero(pos)
        if (viajero.verificar_millas(millas)):
            viajero = millas - viajero 
            self.__viajeros[pos] = viajero
        else:
            print('Error de la Operacion: Millas insuficientes')
        return
    
    def consultar_millas(self):
        num = int(input('Ingrese número de viajero'))
        pos = self.buscar_viajero(num)
        viajero = self.__viajeros[pos]
        return viajero.get_millas()