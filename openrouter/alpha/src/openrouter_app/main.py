import os
from modules.openrouter_client import OpenRouterClient


if __name__ == "__main__":

    # Verificamos que la API key está cargada
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: Configura OPENROUTER_API_KEY en el archivo .env")
        exit(1)

    # Instancia del cliente(openroter)
    client = OpenRouterClient()

    print("-- Prueba LLM Normal (Gratuito) --")
    try:
        respuesta = client.chat_llm("Explícame brevemente qué es OpenRouter.")
        print(f"Respuesta: {respuesta}\n")
    except ValueError as e:
        print(f"Error en LLM: {e}\n")
