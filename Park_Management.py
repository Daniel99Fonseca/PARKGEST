from vehicle import Vehicle
from Park import Park
import Vehicle_Registry
import matplotlib.pyplot as plt


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
        occupied, free = park.vacancy()
        total_free += free
    print(f"Número total de lugares livres: {total_free}\n")


def avg_vacancy_rate():
    avg_rate_all_parks = 0
    for park in park_dict.values():
        avg_rate_all_parks += park.vacancy_rate()
    avg_rate_all_parks /= len(park_dict)
    print(f"Taxa de ocupação média: {avg_rate_all_parks}\n")


def count_private_parks():
    total_parks = len(park_dict)
    private_parks = 0
    for park in park_dict.values():
        if park.is_private:
            private_parks += 1
    percentage = (private_parks / total_parks) * 100
    print(f"{private_parks} ({percentage}:.2f)\n")


# Este código crasha o programa, não dá load
def count_vehicles_by_year():
    vehicles_by_year = {}
    for park in park_dict.values():
        vehicles = park.get_vehicles_in_park()
        for vehicle in vehicles:
            year = vehicle.year
            if vehicle.year in vehicles:
                vehicles_by_year[year] += 1
            else:
                vehicles_by_year[year] = 1
    plt.bar(vehicles_by_year.keys(), vehicles_by_year.values())
    plt.show(block=False)


# def park_dict_graph():
#     park_visualization = []
#     for park in park_dict.values():
#         park_data = {}
#         park_data['position'] = park.location
#         park_data['radius'] =


def view_park_map():
    fig, ax = plt.subplots()
    ax.set_xlim((0, 100))
    ax.set_ylim((0, 100))
    ax.set_box_aspect(1)

    circles = [
        {'position': (10, 10), 'radius': 3.5, 'color': 'r'},
        {'position': (50, 50), 'radius': 8.0, 'color': 'y'},
        {'position': (60, 80), 'radius': 2.0, 'color': 'g'}
    ]

    for c in circles:
        circle = plt.Circle(c['position'], c['radius'], color=c['color'], alpha=0.5)
        ax.add_patch(circle)

    plt.show(block=False)


def stats_info():
    while True:
        print("1. Número total de lugares livres")
        print("2. Taxa de ocupação média")
        print("3. Número de parques privados")
        print("4. Veículos por ano de registo")
        print("5. Visualizar mapa de parques")
        print("0. Voltar\n")
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
                count_vehicles_by_year()
            elif option == 5:
                view_park_map()
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
