class Viajero_frecuente:
    __numero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millasAcum: int
    
    def __init__(self, numero = 0, dni = '', nombre = '', apellido = '', millas_acum = 0):
        self.__numero = numero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millas_acum
        
    def __gt__(self, otroViajero):
        return self.get_millas() > otroViajero.get_millas()
    
    def __eq__(self, millas:int)->bool:
        return self.__millasAcum == millas
    
    def __add__(self, millas:int): 
        return Viajero_frecuente(self.__numero, self.__numero, self.__nombre, self.__apellido, self.__millasAcum + millas)
    
    def __sub__(self, millas:int):
        return Viajero_frecuente(self.__numero, self.__numero, self.__nombre, self.__apellido, self.__millasAcum - millas)

    def __radd__(self, millas:int): 
        return Viajero_frecuente(self.__numero, self.__numero, self.__nombre, self.__apellido, self.__millasAcum + millas)
    
    def __sub__(self, millas:int):
        return Viajero_frecuente(self.__numero, self.__numero, self.__nombre, self.__apellido, self.__millasAcum - millas)
        
    def get_millas(self):
        return self.__millasAcum
    
    def get_numero(self):
        return self.__numero
    
    def get_dni(self)->str:
        return self.__dni
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def verificar_millas(self, millas):
        if (self.__millasAcum >= millas):
            canjearmillas = True
        else:
            canjearmillas = False
        return canjearmillas
    
    def mostrar_datos(self):       
        print ("Datos del Viajero:")
        print ('Numero: {}'.format(self.__numero))
        print ('DNI: '+ self.__dni)
        print ('Nombre y Apellido:' + self.__nombre , self.__apellido)
        print ('Millas Acumuladas: {}'.format(self.__millasAcum))
        print ('')
    