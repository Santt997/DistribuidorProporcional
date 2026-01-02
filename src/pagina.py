#!/usr/bin/python3

# Script para renderizar la pagina con el panel de control
# del Distrubuidor Proporcional
import streamlit as web
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
        web.write(f'Iniciar Sesión en *{self.titular}*')
        mail: str = web.text_input(label = 'Correo Electróncio')
        clave: str = web.text_input(label = 'Clave', type = 'password')
        # Si las claves y mail son correctas devuelve Verdadero sino Falso 
        return (mail == '') and (clave == '')

    def registrar(self) -> bool:
        '''
            Registra usuario con mail,
            clave, alias y cuanto
            recibir del total.

            Devuelve si se registro
            True o False
        '''    
        # Obtener correo a usar
        mail: str = web.text_input(label = 'Correo Electróncio')
        while (mail.__contains__('@') and mail.__contains__('.')):
            mail: str = web.text_input(label = 'Correo Electróncio (mail@sitio)')
        # Obtener clave a usar
        clave: str = web.text_input(label = 'Clave', type = 'password')
        while (clave.__len__() < 8 and not clave.isalnum() and clave.istitle()):
                clave: str = web.text_input(label = 'Clave 8 caracteres, nùmero, simbolo, mayúsculas y minúsculas', type = 'password')
        # Obtener porcentaje del total a recibir        
        total: int = web.slider('Recibir del total 1 a 100')
        while (total < 1 or total > 100):
            total: int = web.slider('Debe ser un porcentaje de 1 a 100')
        # Registrar usuario
        web.write('Anote su mail y clave en un papel por seguridad')
    
        return True    

    def renderizar(self):
        '''
            Define web para mostrar interfaz de 
            usuario.
        '''    
        while not self.iniciar_sesion():
            # Requiere que se inicie la sesion
            if self.registrar():
                # Registro hasta que salga que pueda iniciar sesion
                break
        # Usa el framework y los atributos con los datos necesarios
            
if __name__ == '__main__':
    sitio = Pagina('Distribuidor Proporcional')
    sitio.renderizar()