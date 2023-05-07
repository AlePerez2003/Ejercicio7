from manejador_viajero import Lista_viajero
from viajero import Viajero_frecuente
from menu import Menu

if __name__ == '__main__':
    opciones = Menu()
    listaViajeros = Lista_viajero()
    listaViajeros.test_lista_viajero()
    listaViajeros.mostrar_viajeros()
    num = int(input('Ingrese un número de viajero'))
    pos = listaViajeros.buscar_viajero(num)
    viajero = listaViajeros.get_viajero(pos)
    millas = int(input('Ingrese la cantidad de millas a comparar con el viajero ingresado'))
    if viajero == millas:
        print ('El viajero {} {} tiene la misma cantidad de millas ingresadas'.format(viajero.get_nombre(), viajero.get_apellido()))
        print ('Las millas ingresadas fueron: {}'.format(millas))
    else:
        print ('El viajero {} {} no tiene la misma cantidad de millas ingresadas'.format(viajero.get_nombre(), viajero.get_apellido()))
        print('Las millas ingresadas fueron: {}'.format(millas))
    opciones.menu(listaViajeros)