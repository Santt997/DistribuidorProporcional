class Agrupacion:
    '''
        Agrupa distintos alias para obtener
        lo correspondiente de un alias raiz:

        - miembros, listas de objetos de alias dependientes.
    '''
    def __init__(self):
        
        self.miembros: list[Alias] = []

    def proveer(self) -> None:
        '''
            Hace que alias raiz transfieran
            a sus dependencias
        '''
        for miembro in self.miembros:
            miembro.transferir()   

    def agregar(self, alias: str, corresponde: float) -> None:
        '''
            Agrega nuevo miembro dependiente
            con una correspondencia mayor a
            cero y menor o igual a 1.00 del
            total.
        '''       
        if 0.00 < corresponde <= 1.00:
            # Agrego solo si cumple requerimiento para prevenir problemas
            miembro: Alias = Alias()
            # Defino alias y cuanto le corresponde al miembro
            miembro.corresponde = corresponde
            miembro.alias = alias
            # agrego nuevo miembro
            self.miembros.append(miembro)

class Alias:
    '''
        Define el alias, cuanto le corresponde del total de los
        anteriores y que grupo de alias son posteriores a 
        donde distribuir el monto:

        - monto, real mayor o igual a cero.
        - grupo, objeto con la coleccion de alias posteriores.
        - alias, texto del alias a transferir.
    '''
    def __init__(self):
        # Monto para definir situacion inicial a modificar
        self.monto: float = 0.00
        # Define por defecto que se lleva la mitad del alias que lo agrupe
        self.corresponde: float = 0.50
        # Agrupamiento de diferentes alias posteriores, se va rellenando luego
        self.grupo = Agrupacion()

        self.alias: str = ''

    def transferir(self) -> None:
        '''
            Transfiere lo necesario del
            monto a cada miembro del grupo
        '''
        for miembro in self.grupo.miembros:
            # Realiza la transferencia mientras haya dinero a los primeros del grupo
            if  (
                    self.monto > 0.00 
                    and (0.00 < miembro.corresponde <= 1.00)
                ):
                # transfiere lo que corresponde del monto a miembro del grupo
                miembro.monto += (miembro.corresponde * self.monto)
            elif (self.monto <= 0.00):
                # Nada mas que repartir
                break  

    def agregar(self, alias: str, corresponde: float) -> None:
        '''
            agrega nuevo miembro al grupo
        '''         
        self.grupo.agregar(alias, corresponde)
