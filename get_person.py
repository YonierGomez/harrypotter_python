import requests

def obtener_personaje(URL):
    
    
    r = requests.get(URL)
    
    if r.ok:
        respuesta = r.json()
        
        for r in respuesta:
            print(f'Hola, soy "{r["name"]}" y pertenezco a la casa "{r["name"]}".')

if __name__ == "__main__":
    obtener_personaje(URL = "https://hp-api.onrender.com/api/characters")