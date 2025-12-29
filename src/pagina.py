#!/usr/bin/python3

# Script para renderizar la pagina con el panel de control
# del Distrubuidor Proporcional
from alias import Alias

class Pagina():

    def __init__(self, titulo: str):
        '''
            Usa un framework web para renderizar
            la pàgina, el inicio de sesion,
            el registro de usuarios y el
            objeto que representa al usuario
        '''
        self.titular: str = titulo

        self.usuario: Alias = Alias()

    def iniciar_sesion(self) -> bool:
        '''
            Inica sesion con mail y clave
            de usuario registrado.

            Devuelve si se inicio sesion
            True  o False
        '''    
        pass

    def registrar(self) -> bool:
        '''
            Registra usuario con mail,
            clave, alias y cuanto
            recibir del total.

            Devuelve si se registro
            True o False
        '''    
        pass

    def renderizar(self):
        '''
            Define web para mostrar interfaz de 
            usuario.
        '''    
        while not iniciar_sesion():
            # Requiere que se inicie la sesion
            if registrar():
                # Registro hasta que salga que pueda iniciar sesion
                break
        # Usa el framework y los atributos con los datos necesarios
            
if __name__ == '__main__':
    web = Pagina('Distribuidor Proporcional')
    web.renderizar()