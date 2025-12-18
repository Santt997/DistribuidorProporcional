#!/usr/bin/python3
# Hago estos import para poder usar modulo de carpeta superior
import os
import sys
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)
# Ahora si puedo usar el modulo
from alias import Alias

# Defino los empleados y cuanto le corresponde del total
empleados: dict = {
    'primero' : 0.3,
    'segundo' : 0.25,
    'tercero' : 0.11,
    'cuarto' : 0.34
}
# Define al empleador y su monto
empleador: str = 'Jefe'
# Ingreso en notacion cientifica mas decimales
ingreso: float = 1.2371e4 + 0.25
# Creo objetos para que dependan del empleador
jefe = Alias()
# Configura representacion de la cuenta del jefe
jefe.alias = empleador
jefe.monto = ingreso
# Muestra cuanto hay en total para repartir
print(f'\nEl jefe tiene ${jefe.monto} para repartir a sus empleados:\n')
# Agrega el alias de empleado y cuanto le corresponde del total
for empleado in empleados.keys():
    jefe.agregar(empleado, empleados[empleado])
# Debe transferir o se queda en la cuenta del jefe
jefe.transferir()    
# Muestra cuanto le queda a cada empleado    
for empleado in jefe.grupo.miembros:
    print(f'\tEl empleado "{empleado.alias}" tiene ${round(empleado.monto, 2)}\n')    