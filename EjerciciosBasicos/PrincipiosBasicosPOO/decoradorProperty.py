"""
El decorador puede ser usado sobre un método
, que hará que actúe como si fuera un atributo.
"""
class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo

    @property
    def mi_atributo(self):
        # El acceso se realiza a través de este "método" y
        # podría contener código extra y no un simple retorno
        return self.__mi_atributo

i = Clase("4")
print(i.mi_atributo)
