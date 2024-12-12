import Vehicle_Registry as vr

class Park: # Criação da classe Park
    def __init__(self, name, location, capacity, is_private): # nome, localização, capacidade e acesso (público ou privado)
        self.__name = name
        self.__location = location
        self.__capacity = capacity
        self.__is_private = is_private
        self.__vehicles_in_park = {}
        self.__allowed_plates = [] if is_private else None

# Obter o valor de cada um dos parâmetros da classe Park
    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    @property
    def capacity(self):
        return self.__capacity

    @property
    def is_private(self):
        return self.__is_private

    def is_vehicle_in_park(self, vehicle):
        return vehicle.plate in self.__vehicles_in_park


    def register_entry(self, plate):
        if plate not in vr.vehicles_registry:
            raise Exception("O veículo não existe.")
        vehicle = vr.vehicles_registry[plate]
        if self.is_vehicle_in_park(vehicle):
            raise Exception("O veículo já está no parque.")
        if self.__is_private and vehicle.plate not in self.__allowed_plates:
            raise Exception("O veículo não tem permissão para entrar no parque.")
        if vehicle.category.lower() == "pesado":
            raise Exception("Não são permitidos veículos pesados.")
        if len(self.__vehicles_in_park) >= self.__capacity:
            raise Exception("O Parque está cheio.")
        self.__vehicles_in_park.update({vehicle.plate: vehicle})
        print(f"O veículo com a matrícula {plate} foi adicionado ao parque {self.__name} com sucesso.")

    def register_exit(self, plate):
        if plate not in vr.vehicles_registry:
            raise Exception("O veículo não existe.")
        if plate not in self.__vehicles_in_park:
            raise Exception("O veículo não está no parque.")
        self.__vehicles_in_park.pop(plate)
        print(f"O veículo com a matrícula {plate} foi removido do parque {self.__name}")


    def get_vehicles_in_park(self):
        vehicles = []
        for vehicle in self.__vehicles_in_park.values():
            vehicles.append(vehicle)
        return vehicles

    def list_vehicles_in_park(self):
        for vehicle in self.__vehicles_in_park.values():
            print(vehicle)

    def vacancy(self):  # Demonstração de lugares ocupados e livres
        occupied = len(self.__vehicles_in_park)
        free = self.__capacity - occupied
        return occupied, free

    def vacancy_rate(self):
        occupied = len(self.__vehicles_in_park)
        return occupied / self.__capacity

    def grant_access(self):
        plate = input("Matrícula: ")
        if plate not in self.__allowed_plates:
            self.__allowed_plates.append(plate)
            print(f"Foi concedido acesso ao parque {self.__name} ao veículo com a matrícula {plate}.")
        else:
            print(f"O veículo com a matrícula {plate} já tem acesso ao parque {self.__name}.")

    def vehicles_with_perm(self):
        for vehicle in self.__allowed_plates:
            print(vehicle)

    def revoke_access(self):
        plate = input("Matrícula: ")
        if plate in self.__allowed_plates:
            self.__allowed_plates.remove(plate)
            print(f"O acesso do veículo com a matrícula {plate} foi removido do parque {self.__name}.")
        else:
            print(f"A matrícula {plate} não tem acesso ao parque {self.__name}.")

    def write_to_file(self):
        file_name = input("Ficheiro: ")
        f = open(file_name , "w")
        f.write(str(self))
        for vehicle in self.__vehicles_in_park.values():
            f.write(str(vehicle))
        f.close()

    # Função que transforma um park numa string
    def __str__(self):
        status = "Privado" if self.__is_private else "Público"
        return f"{self.name} ({self.location[0]}, {self.location[1]}) - {status} - {len(self.__vehicles_in_park)} / {self.__capacity}"

    def manage_park(self):
        while True:
            print(f"\n----- GESTÃO DO PARQUE {self.__name} -----")
            print("1. Registar entrada")
            print("2. Registar saída")
            print("3. Listar veículos")
            print("4. Exportar estado")
            if self.__is_private:
                print("5. Listar permissões")
                print("6. Permitir acesso")
                print("7. Revogar acesso")
            print("0. Voltar\n")
            try:
                option = int(input("Opção: "))
            except:
                print("Não foi introduzido um número válido.")
                continue
            try:
                if option == 0:
                    print("A voltar ao menu principal...")
                    break
                elif option == 1:
                    plate = input("Matrícula: ")
                    self.register_entry(plate)
                elif option == 2:
                    plate = input("Matrícula: ")
                    self.register_exit(plate)
                elif option == 3:
                    self.list_vehicles_in_park()
                elif option == 4:
                    self.write_to_file()
                elif option == 5 and self.__is_private:
                    self.vehicles_with_perm()
                elif option == 6 and self.__is_private:
                    self.grant_access()
                elif option == 7 and self.__is_private:
                    self.revoke_access()
                else:
                    print("Opção inválida. Tente novamente.")
            except Exception as exception:
               print(f"Ocorreu um erro: {exception}")