from harry_potter_yonier import get_one_person
if __name__ == "__main__":
    buscar_personaje = input("Ingrese el nombre del personaje que desea buscar: ")
    final = get_one_person.obtener_personaje(URL="https://hp-api.onrender.com/api/characters", PERSONAJE=buscar_personaje)
    print(final)