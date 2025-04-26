import json
import os

# Cargar flujos desde la carpeta flows/
def cargar_flows():
    respuestas = {}
    flows_folder = os.path.join(os.path.dirname(__file__), '..', 'flows')
    
    for archivo in os.listdir(flows_folder):
        if archivo.endswith(".json"):
            with open(os.path.join(flows_folder, archivo), encoding='utf-8') as f:
                flujo = json.load(f)
                for paso in flujo["steps"]:
                    entrada = paso["input"].lower().strip()
                    respuestas[entrada] = paso["response"]
    return respuestas

# Responder entrada del usuario
def responder_entrada(entrada, respuestas):
    entrada_normalizada = entrada.lower().strip()
    return respuestas.get(entrada_normalizada, "Perdón, ¿podés repetirlo? Estoy aprendiendo a entender mejor.")

if __name__ == "__main__":
    respuestas = cargar_flows()
    print("¡Hola! Soy NUMA 🤖💙. Contame, ¿cómo te sentís hoy?")
    while True:
        mensaje = input("Vos: ")
        respuesta = responder_entrada(mensaje, respuestas)
        print("Numa:", respuesta)
