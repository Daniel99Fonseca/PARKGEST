# Criação  da classe veículo
class Vehicle:
    # matrícula,tipo (category),marca,modelo,proprietário,ano_registo
    def __init__(self, plate, category, brand, model, owner, year):
        self.__plate = plate
        self.__category = category
        self.__brand = brand
        self.__model = model
        self.__owner = owner
        self.__year = year

# Obter o valor de cada um dos parâmetros da classe veículo
    @property
    def plate(self):
        return self.__plate

    @property
    def category(self):
        return self.__category

    @property
    def make(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    #Método para alterar o proprietário do veículo
    def change_owner(self, new_owner):
        self.__owner = new_owner

# Função que transforma um veículo numa string
    def __str__(self):
        return f"{self.__plate},{self.__category},{self.__brand},{self.__model},{self.__owner},{self.__year}"

# Função que verifica se dois veículos têm a mesma matrícula
    def __eq__(self, other):
        # Verificação se a comparação são objetos da mesma classe
        if not isinstance(other, self.__class__):
            return False
        # Verificação de matrículas
        return self.__plate == other.__plate