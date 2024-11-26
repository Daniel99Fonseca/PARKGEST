from vehicle import Vehicle
from Park import Park
import Vehicle_Registry

def read_registry(file_name):
    f = open(file_name, "r")
    line = f.readline()  # Leitura linha a linha do ficheiro
    vehicles_dict = {}  #Criação do Dicionário
    while line != '':  # Enquanto houver linhas com texto
        data = line.split(',')  # Agregação dos dados da linha
        plate, category, brand, model, owner, year = data
        vehicle = Vehicle(plate, category, brand, model, owner, int(year))
        vehicles_dict.update({vehicle.plate: vehicle})  # Adicionar veículo ao dicionário
        line = f.readline()  # Leitura da próxima linha
    f.close()
    return vehicles_dict

park_dict = {}

#1. Listar Parques
def list_parks():
    for park in park_dict.values():
        print(park)

#2. Gerir Parque
def manage_specific_park():
    park = input("Introduza o nome do parque: ")
    if park not in park_dict:
        raise Exception("Não existe um parque com esse nome.")
    park = park_dict[park]
    park.manage_park()

def create_park():
    name = input("Nome: ")
    if name in park_dict:
        raise Exception ("Já existe um parque com esse nome.")
    location = input("Localização (latitude, longitude): ").split(",")
    if len(location) != 2:
        raise Exception("Coordenadas inválidas.")
    try:
        latitude = float(location[0])
        longitude = float(location[1])
    except:
        raise Exception("Coordenadas inválidas.")
    if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
        raise Exception("Coordenadas inválidas.")
    capacity = int(input("Capacidade: "))
    if capacity <= 0:
        raise Exception("Capacidade inválida.")
    privacy = input("Privado (s/n): ")
    if not (privacy in ["s" , "n"]):
        raise Exception("Opção inválida.")
    if privacy == "s":
        is_private = True
    else:
        is_private = False
    park = Park(name, location, capacity, is_private)
    park_dict.update({park.name: park})

def remove_park():
    name = input("Nome: ")
    if name not in park_dict:
        raise Exception("Não existe um parque com esse nome.")
    park_dict.pop(name)
    print(f"O parque {name} foi removido")


def total_free_spaces():
    total_free = 0
    for park in park_dict.values():
        occupied = len(park._Park__vehicles_in_park)
        free = park.capacity - occupied
        total_free += free
    print(f"Número total de lugares livres: {total_free}\n")


def avg_vacancy_rate():
    avg_rate_per_park = 0
    for park in park_dict.values():
        avg_rate_per_park += park.vacancy_rate()
    print(f"Taxa de ocupação média: {avg_rate_per_park / len(park_dict)}\n")

def count_private_parks():
    total_parks = len(park_dict)
    private_parks = 0
    for park in park_dict.values():
        if park.is_private:
            private_parks += 1
    percentage = (private_parks / total_parks) * 100
    print(f"{private_parks} ({percentage}%)")


def stats_info():
    while True:
        print("1. Número total de lugares livres")
        print("2. Taxa de ocupação média")
        print("3. Número de parques privados")
        print("4. Veículos por ano de registo")
        print("5. Visualizar mapa de parques")
        print("0. Voltar")
        try:
            option = int(input("Opção: "))
        except:
            print("Não foi introduzido um número válido.")
            continue
        try:
            if option == 0:
                print("A voltar ao menu principal.")
                break
            elif option == 1:
                total_free_spaces()
            elif option == 2:
                avg_vacancy_rate()
            elif option == 3:
                count_private_parks()
            elif option == 4:
                pass
            elif option == 5:
                pass
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as exception:
            print(f"Ocorreu um erro: {exception}")

# Menu principal de gestão de parques
def park_management_menu():
    while True:
        print("\n---PARKGEST---")
        print("1. Listar parques")
        print("2. Gerir parque")
        print("3. Criar parque")
        print("4. Remover parque")
        print("5. Estatísticas e informações")
        print("0. Sair\n")
        try:
            option = int(input("Opção: "))
        except:
            print("Não foi introduzido um número válido.")
            continue
        try:
            if option == 0:
                print("A sair do programa...")
                break
            elif option == 1:
                list_parks()
            elif option == 2:
                manage_specific_park()
            elif option == 3:
                create_park()
            elif option == 4:
                remove_park()
            elif option == 5:
                stats_info()
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as exception:
           print(f"Ocorreu um erro: {exception}")

Vehicle_Registry.vehicles_registry = read_registry('registo.txt')
park_management_menu()