import requests

def obtener_personajes(URL):
    r = requests.get(URL)
    if r.ok:
        respuesta = r.json()
        for personaje in respuesta:
            mensaje = f'Hola, soy "{personaje["name"]}" y pertenezco a la casa "{personaje["house"]}".'
            print(mensaje)

if __name__ == "__main__":
    obtener_personajes(URL="https://hp-api.onrender.com/api/characters")
