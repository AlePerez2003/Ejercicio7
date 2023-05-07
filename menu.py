from manejador_viajero import Lista_viajero

class Menu:
    __cod = int
    
    def __init__(self, cod = 0):
        self.__cod = cod

    def mostrar_menu(self):
        print ('1: Consultar Millas')
        print ('2: Acumular Millas')
        print ('3: Consumir Millas')
        print ('4: Mostrar al/los viajero/s con mayor cantidad de Millas')
        print ('0: Finalizar Operación')
        
    def menu(self, viajeros:Lista_viajero):
        
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el código'))
        
        while self.__cod != 0:
            
            if self.__cod == 1:
                
                self.opcion1(viajeros)
                
            elif self.__cod == 2:
                
                self.opcion2(viajeros)
                
            elif self.__cod == 3:
                
                self.opcion3(viajeros)
                
            elif self.__cod == 4:
                
                self.opcion4(viajeros)
                
            else:
                
                print ('Codigo incorrecto, ingrese de nuevo')
            self.mostrar_menu()
            self.__cod = int(input("Ingrese el código"))
        
        
    def opcion1(self, viajeros):
        
        millas = viajeros.consultar_millas()
        print("El total de millas es:{}".format(millas))
        
    def opcion2(self, viajeros):
        
        viajeros.acumular_millas(int(input('Ingrese cantidad de Millas')))
    
    def opcion3(self, viajeros):
        
        viajeros.canjear_millas(int(input('Ingrese millas a consumir')))
        
    def opcion4(self, viajeros):
        
        viajeros.max_millas()
        