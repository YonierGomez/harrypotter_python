import requests

def obtener_personaje(URL, PERSONAJE):
    r = requests.get(URL)
    
    if r.ok:
        respuesta = r.json()
        
        for r in respuesta:
            if PERSONAJE.lower() in r["name"].lower():
                # print(f"Hola, soy {r['name']} y pertenezco a la casa {r['house']}.")
                return f"Hola, soy {r['name']} y pertenezco a la casa {r['house']}."

if __name__ == "__main__":
    buscar_personaje = input("Ingrese el nombre del personaje que desea buscar: ")
    final = obtener_personaje(URL="https://hp-api.onrender.com/api/characters", PERSONAJE=buscar_personaje)
    print(final)