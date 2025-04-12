
# numa_handler.py

def responder_entrada(entrada):
    respuestas = {
        "hola": "¡Hola! Soy Numa, estoy acá para escucharte. ¿Querés contarme qué te preocupa hoy?",
        "estoy triste": "Siento mucho que te sientas así. ¿Querés hablar de lo que te está pasando?",
        "gracias": "Gracias a vos por confiar. Estoy para acompañarte, cuando quieras."
    }
    entrada_normalizada = entrada.lower().strip()
    return respuestas.get(entrada_normalizada, "Perdón, ¿podés repetirlo? Estoy aprendiendo a entender mejor.")

if __name__ == "__main__":
    while True:
        mensaje = input("Vos: ")
        respuesta = responder_entrada(mensaje)
        print("Numa:", respuesta)
